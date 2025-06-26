import ebooklib
from ebooklib import epub
import html2text
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_epub(epub_path: str) -> str:
    """Process EPUB to extract clean chapter text, prioritizing main content."""
    try:
        book = epub.read_epub(epub_path)
        text = ""
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.ignore_tables = True
        h.body_width = 0
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            name = item.get_name().lower()
            if not any(x in name for x in ["toc", "nav", "meta", "cover", "title", "copyright", "preface", "appendix", "notes"]):
                content = item.get_content().decode('utf-8', errors='ignore')
                cleaned_text = h.handle(content).strip()
                if cleaned_text and len(cleaned_text) > 200:
                    text += cleaned_text + "\n"
        logger.info(f"Processed EPUB content length: {len(text)} characters")
        if not text.strip():
            logger.error("No content extracted from EPUB")
            raise ValueError("Failed to extract EPUB content")
        if len(text) > 150000:
            logger.warning(f"Content size {len(text)} chars exceeds preferred 150,000. Truncating.")
            text = text[:150000]
        return text.strip()
    except Exception as e:
        logger.error(f"Error processing EPUB: {str(e)}")
        raise