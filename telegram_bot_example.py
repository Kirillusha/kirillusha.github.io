# Telegram Bot Example для работы с API

import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# URL вашего API на GitHub Pages
API_BASE_URL = "https://kirillusha.github.io/api"

# Получение данных с API
def get_quotes():
    """Получить все цитаты"""
    response = requests.get(f"{API_BASE_URL}/quotes.json")
    if response.status_code == 200:
        return response.json()["quotes"]
    return []

def get_timeline():
    """Получить хронологию"""
    response = requests.get(f"{API_BASE_URL}/timeline.json")
    if response.status_code == 200:
        return response.json()["events"]
    return []

def get_paintings():
    """Получить картины"""
    response = requests.get(f"{API_BASE_URL}/paintings.json")
    if response.status_code == 200:
        return response.json()["paintings"]
    return []

# Команды бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start"""
    await update.message.reply_text(
        "🎨 Привет! Я бот об Александре Невском.\n\n"
        "Доступные команды:\n"
        "/quote - Случайная цитата\n"
        "/quotes - Все цитаты\n"
        "/timeline - Хронология жизни\n"
        "/paintings - Список картин\n"
        "/painting <номер> - Информация о картине"
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /quote - случайная цитата"""
    quotes = get_quotes()
    if quotes:
        import random
        q = random.choice(quotes)
        await update.message.reply_text(
            f"💭 \"{q['text']}\"\n\n"
            f"— Александр Невский, {q['year']}"
        )
    else:
        await update.message.reply_text("Не удалось получить цитаты 😔")

async def quotes_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /quotes - все цитаты"""
    quotes = get_quotes()
    if quotes:
        text = "📚 Все цитаты Александра Невского:\n\n"
        for q in quotes:
            text += f"{q['id']}. \"{q['text']}\" ({q['year']})\n\n"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Не удалось получить цитаты 😔")

async def timeline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /timeline - хронология"""
    events = get_timeline()
    if events:
        text = "📅 Хронология жизни Александра Невского:\n\n"
        for event in events:
            text += f"🗓 {event['year']} — {event['title']}\n"
            text += f"{event['description']}\n\n"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Не удалось получить хронологию 😔")

async def paintings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /paintings - список картин"""
    paintings = get_paintings()
    if paintings:
        text = "🖼 Картины Александра Невского:\n\n"
        for p in paintings:
            text += f"{p['id']}. {p['title']} ({p['year']})\n"
        text += "\nИспользуйте /painting <номер> для подробностей"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Не удалось получить список картин 😔")

async def painting_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /painting <id> - детали картины"""
    if not context.args:
        await update.message.reply_text("Укажите номер картины: /painting 1")
        return
    
    try:
        painting_id = int(context.args[0])
        paintings = get_paintings()
        painting = next((p for p in paintings if p['id'] == painting_id), None)
        
        if painting:
            text = f"🎨 {painting['title']}\n\n"
            text += f"📅 Год: {painting['year']}\n"
            text += f"📍 Местонахождение: {painting['location']}\n"
            text += f"🎨 Цвета: {', '.join(painting['colors'])}\n\n"
            text += f"📝 {painting['description']}"
            await update.message.reply_text(text)
        else:
            await update.message.reply_text(f"Картина #{painting_id} не найдена")
    except ValueError:
        await update.message.reply_text("Неверный формат. Используйте: /painting 1")

def main():
    """Запуск бота"""
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("quotes", quotes_all))
    application.add_handler(CommandHandler("timeline", timeline))
    application.add_handler(CommandHandler("paintings", paintings))
    application.add_handler(CommandHandler("painting", painting_detail))
    
    # Запуск бота
    print("Бот запущен!")
    application.run_polling()

if __name__ == "__main__":
    main()
