from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

router = Router()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Чеклист")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для работы с EPUB книгами. Отправь мне файл .epub, и я предложу варианты обработки. Либо выбери одно из предложенных действий ниже",
        reply_markup=keyboard
    )