from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.states import UserState

router = Router()

@router.message(Command("lang"))
async def select_language(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="English", callback_data="lang_en"),
            InlineKeyboardButton(text="Русский", callback_data="lang_ru"),
        ]
    ])
    await message.answer("Please select a language / Пожалуйста, выберите язык:", reply_markup=keyboard)

@router.callback_query(lambda c: c.data.startswith("lang_"))
async def process_language(callback: CallbackQuery, state: FSMContext):
    language = "en" if callback.data == "lang_en" else "ru"
    await state.update_data(language=language)
    await callback.message.answer(
        f"Language set to {'English' if language == 'en' else 'Русский'}."
    )
    await callback.answer()
