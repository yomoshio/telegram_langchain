from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_deepseek.chat_models import ChatDeepSeek
from bot.services.pdf_generator import generate_pdf
from bot.config.settings import settings
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
import asyncio
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DeepSeekService:
    def __init__(self):
        self.llm = ChatDeepSeek(
            api_key=settings.DEEPSEEK_API_KEY,
            model="deepseek-reasoner",
            timeout=1200,
            max_tokens=8000
        )
        self.prompt_template = PromptTemplate(
            input_variables=["content", "instructions"],
            template="Content: {content}\n\nInstructions: {instructions}"
        )
        self.chain = self.prompt_template | self.llm
        self.max_input_tokens = 65536
        self.chars_per_token = 4
        self.min_word_count_part = 1500
        self.max_word_count_part = 3500
        self.min_word_count_total = 3000
        self.max_word_count_total = 7000
        self.semaphore = asyncio.Semaphore(30)

    def _estimate_tokens(self, text: str) -> int:
        return len(text) // self.chars_per_token + 1

    def _count_words(self, text: str) -> int:
        return len(re.findall(r'\w+', text))

    def _truncate_content(self, content: str, instructions: str) -> str:
        prompt_tokens = self._estimate_tokens(instructions)
        max_content_tokens = self.max_input_tokens - prompt_tokens - 1000
        max_content_chars = max_content_tokens * self.chars_per_token
        if len(content) <= max_content_chars:
            return content
        logger.warning(f"Truncating content from {len(content)} to {max_content_chars} chars")
        return content[:max_content_chars]

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _generate_content(self, content: str, instructions: str, module_range: str) -> str:
        logger.info(f"Generating content for modules {module_range}")
        async with self.semaphore:
            try:
                modified_instructions = (
                    f"{instructions}\n\n"
                    f"Focus on generating detailed, comprehensive content for modules {module_range}, "
                    f"targeting approximately {self.min_word_count_part}-{self.max_word_count_part} words. "
                    f"Ensure all required components (e.g., tables, exercises, case studies) are included with rich examples. "
                    f"If output is shorter, prioritize depth and specificity over strict word count."
                )
                input_data = {"content": content, "instructions": modified_instructions}
                response = await self.chain.ainvoke(input_data)
                generated_text = response.content if hasattr(response, 'content') else str(response)
                word_count = self._count_words(generated_text)
                logger.info(f"Generated {len(generated_text)} chars, {word_count} words for modules {module_range}")
                if word_count < 1500:
                    logger.warning(f"Output critically short: {word_count} words (target {self.min_word_count_part})")
                return generated_text
            except Exception as e:
                logger.error(f"Error generating content for modules {module_range}: {str(e)}")
                raise

    async def _generate_part(self, content: str, instructions: str, module_range: str) -> str:
        logger.info(f"Generating part for modules {module_range}")
        truncated_content = self._truncate_content(content, instructions)
        try:
            generated_text = await self._generate_content(truncated_content, instructions, module_range)
            word_count = self._count_words(generated_text)
            if word_count >= self.min_word_count_part:
                logger.info(f"Part meets target: {word_count} words for modules {module_range}")
                return generated_text
            logger.warning(f"Part output short: {word_count} words (target {self.min_word_count_part}). Attempting chunking.")
        except Exception as e:
            logger.warning(f"Part generation failed: {str(e)}. Attempting chunking.")

        max_chunk_chars = 50000
        content_chunks = [content[i:i + max_chunk_chars] for i in range(0, len(content), max_chunk_chars)]
        logger.info(f"Split into {len(content_chunks)} chunks of ~{max_chunk_chars} chars for modules {module_range}")

        chunk_module_ranges = [f"{module_range}-chunk{i+1}" for i in range(len(content_chunks))]
        tasks = [
            self._generate_content(chunk, instructions, chunk_range)
            for chunk, chunk_range in zip(content_chunks, chunk_module_ranges)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        generated_text = ""
        total_word_count = 0
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                logger.warning(f"Chunk {i + 1} (modules {chunk_module_ranges[i]}) failed: {str(result)}. Skipping.")
                continue
            generated_text += result + "\n\n"
            chunk_word_count = self._count_words(result)
            total_word_count += chunk_word_count
            logger.info(f"Chunk {i + 1} generated {chunk_word_count} words for modules {chunk_module_ranges[i]}")

        logger.info(f"Combined part output: {total_word_count} words for modules {module_range}")
        if total_word_count < 1500:
            logger.warning(f"Combined part critically short: {total_word_count} words (target {self.min_word_count_part})")
        return generated_text

    async def generate_pdf_parts(self, content: str, instructions: str, output_path: str) -> list:
        logger.info(f"Starting PDF generation for {output_path}")
        try:
            async with self.semaphore:
                tasks = [
                    self._generate_part(content, instructions, "1-4"),
                    self._generate_part(content, instructions, "5-8")
                ]
                parts = await asyncio.gather(*tasks, return_exceptions=True)
            

            for i, part in enumerate(parts, 1):
                if isinstance(part, Exception):
                    logger.error(f"Error generating part {i} (Modules {['1-4', '5-8'][i-1]}): {str(part)}")
                    raise part

            total_word_count = sum(self._count_words(part) for part in parts)
            logger.info(f"Total output: {total_word_count} words")
            if total_word_count < self.min_word_count_total:
                logger.warning(f"Total output short: {total_word_count} words (target {self.min_word_count_total})")


            combined_content = parts[0] + "\n\n---\n\n" + parts[1]
            logger.info(f"Rendering single PDF at {output_path}")
            pdf_path = generate_pdf(combined_content, output_path)
            logger.info(f"PDF generated at {pdf_path}")
            return [pdf_path]
        except Exception as e:
            logger.error(f"Error in PDF generation: {str(e)}")
            raise

    async def generate_pdf(self, content: str, instructions: str, output_path: str) -> str:
        logger.info(f"Starting single PDF generation for {output_path}")
        try:
            truncated_content = self._truncate_content(content, instructions)
            generated_text = await self._generate_content(truncated_content, instructions, "all")
            word_count = self._count_words(generated_text)
            logger.info(f"Generated {word_count} words for single PDF")
            if word_count < 1500:
                logger.warning(f"Single PDF output short: {word_count} words (target 2500-5000)")
            pdf_path = generate_pdf(generated_text, output_path)
            logger.info(f"PDF generated at {pdf_path}")
            return pdf_path
        except Exception as e:
            logger.error(f"Error in single PDF generation: {str(e)}")
            raise
