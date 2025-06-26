from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_action_buttons() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Сделать конспект", callback_data="summary"),
            InlineKeyboardButton(text="Тетрадь с заданиями", callback_data="worksheet")
        ],
        [
            InlineKeyboardButton(text="Создать тест", callback_data="quiz"),
            InlineKeyboardButton(text="Литературный анализ", callback_data="analysis")
        ]
    ])