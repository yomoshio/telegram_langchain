from aiogram import Router, F
from aiogram.types import Message, Document
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.utils.keyboard import get_action_buttons
import os

router = Router()

class EpubStates(StatesGroup):
    waiting_for_epub = State()
    processing = State()

@router.message(F.document.mime_type == "application/epub+zip")
async def handle_epub(message: Message, state: FSMContext):
    document: Document = message.document
    file_info = await message.bot.get_file(document.file_id)
    file_path = f"temp/{document.file_name}"
    
    os.makedirs("temp", exist_ok=True)
    await message.bot.download_file(file_info.file_path, file_path)
    
    await state.update_data(epub_path=file_path)
    await message.answer(
        "Книга загружена! Выберите действие:",
        reply_markup=get_action_buttons()
    )
    await state.set_state(EpubStates.processing)