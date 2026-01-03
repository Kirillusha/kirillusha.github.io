# Telegram Bot с локальным и удаленным API (aiogram 3)

import asyncio
import random
import logging
import os
import json
from pathlib import Path
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.enums import ParseMode
import aiohttp

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# URL вашего API на GitHub Pages
API_BASE_URL = "https://kirillusha.github.io/api"

# Путь к локальным файлам (для тестирования)
LOCAL_API_PATH = Path(__file__).parent / "api"

# Режим работы: local или remote
USE_LOCAL_API = True  # Установите False когда опубликуете на GitHub Pages

# Роутер для обработки команд
router = Router()

# Получение данных с API (с поддержкой локального режима)
async def get_data_from_file(filename: str):
    """Получить данные из локального файла"""
    try:
        file_path = LOCAL_API_PATH / filename
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            logger.error(f"Локальный файл не найден: {file_path}")
    except Exception as e:
        logger.error(f"Ошибка чтения локального файла {filename}: {e}")
    return None

async def get_data_from_url(url: str):
    """Получить данные из удаленного API"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.error(f"HTTP {response.status} при запросе к {url}")
        except asyncio.TimeoutError:
            logger.error(f"Таймаут при запросе к {url}")
        except Exception as e:
            logger.error(f"Ошибка запроса к {url}: {e}")
    return None

async def get_quotes():
    """Получить все цитаты"""
    if USE_LOCAL_API:
        logger.info("Используется локальный API для quotes")
        data = await get_data_from_file("quotes.json")
    else:
        logger.info("Используется удаленный API для quotes")
        data = await get_data_from_url(f"{API_BASE_URL}/quotes.json")
    
    return data.get("quotes", []) if data else []

async def get_timeline():
    """Получить хронологию"""
    if USE_LOCAL_API:
        logger.info("Используется локальный API для timeline")
        data = await get_data_from_file("timeline.json")
    else:
        logger.info("Используется удаленный API для timeline")
        data = await get_data_from_url(f"{API_BASE_URL}/timeline.json")
    
    return data.get("events", []) if data else []

async def get_paintings():
    """Получить картины"""
    if USE_LOCAL_API:
        logger.info("Используется локальный API для paintings")
        data = await get_data_from_file("paintings.json")
    else:
        logger.info("Используется удаленный API для paintings")
        data = await get_data_from_url(f"{API_BASE_URL}/paintings.json")
    
    return data.get("paintings", []) if data else []

# Команды бота
@router.message(Command("start"))
async def cmd_start(message: Message):
    """Команда /start"""
    mode = "локальный" if USE_LOCAL_API else "удаленный"
    await message.answer(
        f"🎨 <b>Привет! Я бот об Александре Невском.</b>\n\n"
        f"<i>Режим API: {mode}</i>\n\n"
        "Доступные команды:\n"
        "/quote - Случайная цитата\n"
        "/quotes - Все цитаты\n"
        "/timeline - Хронология жизни\n"
        "/paintings - Список картин\n"
        "/painting &lt;номер&gt; - Информация о картине\n"
        "/mode - Переключить режим API",
        parse_mode=ParseMode.HTML
    )

@router.message(Command("mode"))
async def cmd_mode(message: Message):
    """Команда /mode - переключить режим API"""
    global USE_LOCAL_API
    USE_LOCAL_API = not USE_LOCAL_API
    mode = "локальный" if USE_LOCAL_API else "удаленный"
    await message.answer(
        f"✅ Режим API изменен на: <b>{mode}</b>",
        parse_mode=ParseMode.HTML
    )

@router.message(Command("quote"))
async def cmd_quote(message: Message):
    """Команда /quote - случайная цитата"""
    quotes = await get_quotes()
    if quotes:
        q = random.choice(quotes)
        await message.answer(
            f"💭 <i>\"{q['text']}\"</i>\n\n"
            f"— Александр Невский, {q['year']}",
            parse_mode=ParseMode.HTML
        )
    else:
        await message.answer(
            "❌ Не удалось получить цитаты 😔\n\n"
            "Проверьте:\n"
            "1. Если USE_LOCAL_API=True, проверьте наличие файла api/quotes.json\n"
            "2. Если USE_LOCAL_API=False, проверьте что сайт опубликован на GitHub Pages"
        )

@router.message(Command("quotes"))
async def cmd_quotes_all(message: Message):
    """Команда /quotes - все цитаты"""
    quotes = await get_quotes()
    if quotes:
        text = "📚 <b>Все цитаты Александра Невского:</b>\n\n"
        for q in quotes:
            text += f"{q['id']}. <i>\"{q['text']}\"</i> ({q['year']})\n\n"
        await message.answer(text, parse_mode=ParseMode.HTML)
    else:
        await message.answer(
            "❌ Не удалось получить цитаты 😔\n\n"
            "Используйте /mode для переключения режима API"
        )

@router.message(Command("timeline"))
async def cmd_timeline(message: Message):
    """Команда /timeline - хронология"""
    events = await get_timeline()
    if events:
        text = "📅 <b>Хронология жизни Александра Невского:</b>\n\n"
        for event in events:
            text += f"🗓 <b>{event['year']}</b> — {event['title']}\n"
            text += f"{event['description']}\n\n"
        await message.answer(text, parse_mode=ParseMode.HTML)
    else:
        await message.answer(
            "❌ Не удалось получить хронологию 😔\n\n"
            "Используйте /mode для переключения режима API"
        )

@router.message(Command("paintings"))
async def cmd_paintings(message: Message):
    """Команда /paintings - список картин"""
    paintings = await get_paintings()
    if paintings:
        text = "🖼 <b>Картины Александра Невского:</b>\n\n"
        for p in paintings:
            text += f"{p['id']}. <b>{p['title']}</b> ({p['year']})\n"
        text += "\nИспользуйте /painting &lt;номер&gt; для подробностей"
        await message.answer(text, parse_mode=ParseMode.HTML)
    else:
        await message.answer(
            "❌ Не удалось получить список картин 😔\n\n"
            "Используйте /mode для переключения режима API"
        )

@router.message(Command("painting"))
async def cmd_painting_detail(message: Message, command: CommandObject):
    """Команда /painting <id> - детали картины"""
    if not command.args:
        await message.answer("Укажите номер картины: /painting 1")
        return
    
    try:
        painting_id = int(command.args.split()[0])
        paintings = await get_paintings()
        painting = next((p for p in paintings if p['id'] == painting_id), None)
        
        if painting:
            text = f"🎨 <b>{painting['title']}</b>\n\n"
            text += f"📅 Год: {painting['year']}\n"
            text += f"📍 Местонахождение: {painting['location']}\n"
            text += f"🎨 Цвета: {', '.join(painting['colors'])}\n\n"
            text += f"📝 {painting['description']}"
            await message.answer(text, parse_mode=ParseMode.HTML)
        else:
            await message.answer(f"Картина #{painting_id} не найдена")
    except (ValueError, IndexError):
        await message.answer("Неверный формат. Используйте: /painting 1")

async def main():
    """Запуск бота"""
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    bot = Bot(token="YOUR_BOT_TOKEN")
    dp = Dispatcher()
    
    # Подключаем роутер
    dp.include_router(router)
    
    # Проверка локальных файлов при запуске
    if USE_LOCAL_API:
        logger.info(f"🔧 Режим: ЛОКАЛЬНЫЙ API")
        logger.info(f"📁 Путь к API: {LOCAL_API_PATH}")
        if not LOCAL_API_PATH.exists():
            logger.error(f"❌ Папка {LOCAL_API_PATH} не найдена!")
        else:
            logger.info(f"✅ Папка API найдена")
    else:
        logger.info(f"🌐 Режим: УДАЛЕННЫЙ API")
        logger.info(f"🔗 URL: {API_BASE_URL}")
    
    # Запуск бота
    logger.info("🚀 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
