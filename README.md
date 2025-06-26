# Telegram EPUB Processing Bot

A Telegram bot that processes EPUB files and generates PDF documents using DeepSeek and LangChain.

## Features
- Upload EPUB files
- Generate:
  - Book summary
  - Worksheet with tasks
  - Multiple-choice quiz
  - Literary analysis
- PDF output for all generated content

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in:
   - `BOT_TOKEN`: Your Telegram bot token
   - `DEEPSEEK_API_KEY`: Your DeepSeek API key
4. Run the bot: `python -m bot.main`

## Project Structure
- `bot/main.py`: Entry point
- `bot/handlers/`: Telegram command and callback handlers
- `bot/services/`: EPUB processing, PDF generation, and DeepSeek integration
- `bot/utils/`: Prompts and keyboard utilities
- `bot/config/`: Configuration management

## Notes
- Replace the DeepSeek placeholder in `deepseek_service.py` with actual API integration
- Ensure sufficient memory for processing large EPUB files
- Temporary files are stored in `temp/` directory