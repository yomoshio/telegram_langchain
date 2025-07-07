import os
import asyncio
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from bot.services.deepseek_checklist_service import ChecklistService
from bot.services.pdf_generator import generate_pdf
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = Router()
checklist_service = ChecklistService()  # Initialize the service

# Define states
class ChecklistStates(StatesGroup):
    awaiting_request = State()
    processing = State()


@router.message(F.text == "Чеклист")
async def checklist_start(message: Message, state: FSMContext):
    """Handle 'Checklist' button press."""
    await state.set_state(ChecklistStates.awaiting_request)
    await message.answer("Пожалуйста, уточните, для какой задачи нужен чек-лист? Укажите детали задачи.")

@router.message(ChecklistStates.awaiting_request)
async def process_request(message: Message, state: FSMContext):
    """Process the user's checklist request and send a PDF."""
    await state.set_state(ChecklistStates.processing)
    user_request = message.text
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    pdf_path = os.path.join(temp_dir, f"checklist_{message.from_user.id}_{message.message_id}.pdf")

    try:
        # Generate checklist text and PDF
        checklist_content = await checklist_service.generate_checklist_text(user_request)
        pdf_path = generate_pdf(checklist_content, pdf_path)
        
        # Send the PDF to the user
        await message.answer_document(FSInputFile(pdf_path, filename="checklist.pdf"))
        logger.info(f"Sent PDF to user {message.from_user.id} at {pdf_path}")
    except Exception as e:
        logger.error(f"Error processing request for user {message.from_user.id}: {str(e)}")
        await message.answer("Произошла ошибка при создании чек-листа. Пожалуйста, попробуйте еще раз.")
    finally:
        # Clean up the temporary PDF file
        try:
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
                logger.info(f"Deleted temporary PDF: {pdf_path}")
        except Exception as e:
            logger.warning(f"Failed to delete temporary PDF {pdf_path}: {str(e)}")
        await state.clear()

@router.message(Command("checklist"))
async def checklist_command(message: Message, state: FSMContext):
    """Handle /checklist command."""
    await checklist_start(message, state)