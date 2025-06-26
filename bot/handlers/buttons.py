from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from bot.services.epub_processor import process_epub
from bot.services.deepseek_service import DeepSeekService
from bot.utils.prompts import SUMMARY_PROMPT_EN, WORKSHEET_PROMPT_EN, QUIZ_PROMPT_EN, ANALYSIS_PROMPT_EN
from bot.utils.prompts import SUMMARY_PROMPT_RU, WORKSHEET_PROMPT_RU, QUIZ_PROMPT_RU, ANALYSIS_PROMPT_RU
import os
import logging
import asyncio

router = Router()
logger = logging.getLogger(__name__)

@router.callback_query(F.data == "summary")
async def process_summary(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    language = data.get("language", "en")
    status_msg = await callback.message.answer(
        "Обрабатываю EPUB..." if language == "ru" else "Processing EPUB..."
    )
    
    try:
        epub_path = data.get("epub_path")
        if not epub_path or not os.path.exists(epub_path):
            await status_msg.edit_text(
                "Ошибка: EPUB файл не найден." if language == "ru" else "Error: EPUB file not found."
            )
            return
        
        await status_msg.edit_text(
            "Извлекаю содержимое EPUB..." if language == "ru" else "Extracting EPUB content..."
        )
        content = process_epub(epub_path)
        
        await status_msg.edit_text(
            "Генерирую конспект (Модули 1-8)..." if language == "ru" else 
            "Generating summary (Modules 1-8)..."
        )
        deepseek = DeepSeekService()
        prompt = SUMMARY_PROMPT_RU if language == "ru" else SUMMARY_PROMPT_EN
        output_path = f"temp/summary_{callback.message.chat.id}.pdf"
        
        await status_msg.edit_text(
            "Генерирую PDF конспекта..." if language == "ru" else 
            "Generating summary PDF..."
        )
        pdf_paths = await deepseek.generate_pdf_parts(content, prompt, output_path)
        
        await status_msg.edit_text(
            "Загружаю PDF конспекта..." if language == "ru" else 
            "Uploading summary PDF..."
        )
        for pdf_path in pdf_paths:
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as pdf_file:
                    await callback.message.answer_document(
                        document=FSInputFile(pdf_path, filename="summary.pdf")
                    )
                os.remove(pdf_path)
            else:
                logger.warning(f"PDF not found at {pdf_path}")
        
        await status_msg.edit_text(
            "Конспект готов! Отправьте новый EPUB или выберите другое действие." if language == "ru" else 
            "Summary ready! Send a new EPUB or choose another action."
        )
    except Exception as e:
        logger.error(f"Error processing summary: {str(e)}")
        await status_msg.edit_text(
            f"Ошибка: {str(e)}. Пожалуйста, попробуйте снова." if language == "ru" else 
            f"Error: {str(e)}. Please try again."
        )

@router.callback_query(F.data == "worksheet")
async def process_worksheet(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    language = data.get("language", "en")
    status_msg = await callback.message.answer(
        "Обрабатываю EPUB..." if language == "ru" else "Processing EPUB..."
    )
    
    try:
        epub_path = data.get("epub_path")
        if not epub_path or not os.path.exists(epub_path):
            await status_msg.edit_text(
                "Ошибка: EPUB файл не найден." if language == "ru" else "Error: EPUB file not found."
            )
            return
        
        await status_msg.edit_text(
            "Извлекаю содержимое EPUB..." if language == "ru" else "Extracting EPUB content..."
        )
        content = process_epub(epub_path)
        
        await status_msg.edit_text(
            "Генерирую тетрадь с заданиями..." if language == "ru" else "Generating worksheet..."
        )
        deepseek = DeepSeekService()
        prompt = WORKSHEET_PROMPT_RU if language == "ru" else WORKSHEET_PROMPT_EN
        pdf_path = await deepseek.generate_pdf(content, prompt, f"temp/worksheet_{callback.message.chat.id}.pdf")
        
        await status_msg.edit_text(
            "Загружаю PDF тетради..." if language == "ru" else "Uploading worksheet PDF..."
        )
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                await callback.message.answer_document(
                    document=FSInputFile(pdf_path, filename="worksheet.pdf")
                )
            os.remove(pdf_path)
        
        await status_msg.edit_text(
            "Тетрадь готова! Отправьте новый EPUB или выберите другое действие." if language == "ru" else 
            "Worksheet ready! Send a new EPUB or choose another action."
        )
    except Exception as e:
        logger.error(f"Error processing worksheet: {str(e)}")
        await status_msg.edit_text(
            f"Ошибка: {str(e)}. Пожалуйста, попробуйте снова." if language == "ru" else 
            f"Error: {str(e)}. Please try again."
        )

@router.callback_query(F.data == "quiz")
async def process_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    language = data.get("language", "en")
    status_msg = await callback.message.answer(
        "Обрабатываю EPUB..." if language == "ru" else "Processing EPUB..."
    )
    
    try:
        epub_path = data.get("epub_path")
        if not epub_path or not os.path.exists(epub_path):
            await status_msg.edit_text(
                "Ошибка: EPUB файл не найден." if language == "ru" else "Error: EPUB file not found."
            )
            return
        
        await status_msg.edit_text(
            "Извлекаю содержимое EPUB..." if language == "ru" else "Extracting EPUB content..."
        )
        content = process_epub(epub_path)
        
        await status_msg.edit_text(
            "Генерирую тест..." if language == "ru" else "Generating quiz..."
        )
        deepseek = DeepSeekService()
        prompt = QUIZ_PROMPT_RU if language == "ru" else QUIZ_PROMPT_EN
        pdf_path = await deepseek.generate_pdf(content, prompt, f"temp/quiz_{callback.message.chat.id}.pdf")
        
        await status_msg.edit_text(
            "Загружаю PDF теста..." if language == "ru" else "Uploading quiz PDF..."
        )
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                await callback.message.answer_document(
                    document=FSInputFile(pdf_path, filename="quiz.pdf")
                )
            os.remove(pdf_path)
        
        await status_msg.edit_text(
            "Тест готов! Отправьте новый EPUB или выберите другое действие." if language == "ru" else 
            "Quiz ready! Send a new EPUB or choose another action."
        )
    except Exception as e:
        logger.error(f"Error processing quiz: {str(e)}")
        await status_msg.edit_text(
            f"Ошибка: {str(e)}. Пожалуйста, попробуйте снова." if language == "ru" else 
            f"Error: {str(e)}. Please try again."
        )

@router.callback_query(F.data == "analysis")
async def process_analysis(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    language = data.get("language", "en")
    status_msg = await callback.message.answer(
        "Обрабатываю EPUB..." if language == "ru" else "Processing EPUB..."
    )
    
    try:
        epub_path = data.get("epub_path")
        if not epub_path or not os.path.exists(epub_path):
            await status_msg.edit_text(
                "Ошибка: EPUB файл не найден." if language == "ru" else "Error: EPUB file not found."
            )
            return
        
        await status_msg.edit_text(
            "Извлекаю содержимое EPUB..." if language == "ru" else "Extracting EPUB content..."
        )
        content = process_epub(epub_path)
        
        await status_msg.edit_text(
            "Генерирую анализ..." if language == "ru" else "Generating analysis..."
        )
        deepseek = DeepSeekService()
        prompt = ANALYSIS_PROMPT_RU if language == "ru" else ANALYSIS_PROMPT_EN
        pdf_path = await deepseek.generate_pdf(content, prompt, f"temp/analysis_{callback.message.chat.id}.pdf")
        
        await status_msg.edit_text(
            "Загружаю PDF анализа..." if language == "ru" else "Uploading analysis PDF..."
        )
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                await callback.message.answer_document(
                    document=FSInputFile(pdf_path, filename="analysis.pdf")
                )
            os.remove(pdf_path)
        
        await status_msg.edit_text(
            "Анализ готов! Отправьте новый EPUB или выберите другое действие." if language == "ru" else 
            "Analysis ready! Send a new EPUB or choose another action."
        )
    except Exception as e:
        logger.error(f"Error processing analysis: {str(e)}")
        await status_msg.edit_text(
            f"Ошибка: {str(e)}. Пожалуйста, попробуйте снова." if language == "ru" else 
            f"Error: {str(e)}. Please try again."
        )
