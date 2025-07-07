import os
from openai import OpenAI
from bot.config.settings import settings
from bot.services.pdf_generator import generate_pdf
import logging
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ChecklistService:
    def __init__(self):
        """Initialize the OpenAI client for DeepSeek API and system prompt."""
        self.client = OpenAI(
            api_key=settings.DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com"
        )
        self.system_prompt = """
Ты специалист по созданию проверочных списков и чек-листов для любой задачи.
Ты получаешь запрос пользователя и выполняешь задачу по созданию чек-листа следующим образом:

1. Разбиваешь задачу на этапы в необходимой временной последовательности: с чего начать и как закончить, чтобы задача была выполнена достаточно хорошо для 95% ситуаций.
2. Каждый этап имеет свое название, краткое пояснение, зачем нужен данный этап и какие ресурсы необходимы для выполнения данного этапа (финансы, время, оборудование, компоненты, ингредиенты, внешние специалисты, время, действия и другое, в зависимости от конкретной задачи).
3. Для каждого этапа ты создаешь чек-лист последовательных действий.
4. Придерживайся текстов без излишней эмоциональной или художественной окраски.
"""

    async def generate_checklist_text(self, user_prompt: str) -> str:
        """Generate checklist text based on the user prompt."""
        logger.info(f"Generating checklist text for prompt: {user_prompt}")
        try:
            response = await asyncio.to_thread(self.client.chat.completions.create,
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=8000,
                stream=False
            )
            generated_text = response.choices[0].message.content
            logger.info("Checklist text generated successfully")
            return generated_text
        except Exception as e:
            logger.error(f"Error generating checklist text: {str(e)}")
            raise

    async def generate_checklist_pdf(self, user_prompt: str, output_path: str) -> str:
        """Generate a PDF from the checklist text."""
        logger.info(f"Starting PDF generation for: {output_path}")
        try:
            checklist_text = await self.generate_checklist_text(user_prompt)
            pdf_path = generate_pdf(checklist_text, output_path)
            logger.info(f"PDF generated at {pdf_path}")
            return pdf_path
        except Exception as e:
            logger.error(f"Error in PDF generation: {str(e)}")
            raise

# Example usage
async def main():
    service = ChecklistService()
    user_prompt = "Создай чек-лист для подготовки к переезду в новую квартиру"
    output_path = "checklist.pdf"
    pdf_path = await service.generate_checklist_pdf(user_prompt, output_path)
    print(f"PDF generated at: {pdf_path}")

if __name__ == "__main__":
    asyncio.run(main())