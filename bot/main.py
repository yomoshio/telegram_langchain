import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.config.settings import settings
from bot.handlers import start, epub, buttons, language, checklist

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    

    dp.include_routers(start.router, epub.router, buttons.router, language.router, checklist.router)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
#sssss
if __name__ == "__main__":
    asyncio.run(main())