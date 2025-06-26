from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для работы с EPUB книгами. Отправь мне файл .epub, и я предложу варианты обработки."
    )