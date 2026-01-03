# Telegram Bot Example для работы с API (aiogram 3)

import asyncio
import random
import logging
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

# Роутер для обработки команд
router = Router()

# Получение данных с API (асинхронно)
async def get_quotes():
    """Получить все цитаты"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL}/quotes.json") as response:
                if response.status == 200:
                    data = await response.json()
                    return data["quotes"]
        except Exception as e:
            logger.error(f"Ошибка получения цитат: {e}")
    return []

async def get_timeline():
    """Получить хронологию"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL}/timeline.json") as response:
                if response.status == 200:
                    data = await response.json()
                    return data["events"]
        except Exception as e:
            logger.error(f"Ошибка получения хронологии: {e}")
    return []

async def get_paintings():
    """Получить картины"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_BASE_URL}/paintings.json") as response:
                if response.status == 200:
                    data = await response.json()
                    return data["paintings"]
        except Exception as e:
            logger.error(f"Ошибка получения картин: {e}")
    return []

# Команды бота
@router.message(Command("start"))
async def cmd_start(message: Message):
    """Команда /start"""
    await message.answer(
        "🎨 <b>Привет! Я бот об Александре Невском.</b>\n\n"
        "Доступные команды:\n"
        "/quote - Случайная цитата\n"
        "/quotes - Все цитаты\n"
        "/timeline - Хронология жизни\n"
        "/paintings - Список картин\n"
        "/painting &lt;номер&gt; - Информация о картине",
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
        await message.answer("Не удалось получить цитаты 😔")

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
        await message.answer("Не удалось получить цитаты 😔")

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
        await message.answer("Не удалось получить хронологию 😔")

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
        await message.answer("Не удалось получить список картин 😔")

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
    
    # Запуск бота
    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
