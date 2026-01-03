# kirillusha.github.io

Веб-сайт об Александре Невском с API для Telegram бота.

## 🌐 Сайт
**URL:** https://kirillusha.github.io

Интерактивный сайт о вымышленном художнике Александре Невском.

## 🤖 Telegram Bot API

API для создания Telegram ботов с информацией о художнике.

### Эндпоинты:
- `/api/quotes.json` - Цитаты
- `/api/timeline.json` - Хронология жизни
- `/api/paintings.json` - Картины
- `/api/index.json` - Список всех эндпоинтов

### Пример использования:
```python
import aiohttp

async def get_quotes():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://kirillusha.github.io/api/quotes.json") as response:
            data = await response.json()
            return data["quotes"]
```

## 📦 Файлы проекта

- `index.html` - Главная страница сайта
- `api/` - API эндпоинты для Telegram бота
- `telegram_bot_example.py` - Пример Telegram бота на aiogram 3
- `TELEGRAM_BOT_SETUP.md` - Инструкция по настройке бота

## 🚀 Как использовать

### Для просмотра сайта:
Просто откройте https://kirillusha.github.io

### Для запуска Telegram бота:

1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Создайте бота через @BotFather**

3. **Настройте токен в `telegram_bot_example.py`:**
   ```python
   bot = Bot(token="YOUR_BOT_TOKEN")
   ```

4. **Запустите:**
   ```bash
   python telegram_bot_example.py
   ```

**Подробная инструкция:** См. [TELEGRAM_BOT_SETUP.md](TELEGRAM_BOT_SETUP.md)

## 🔄 Режимы работы бота

### Локальный режим (по умолчанию)
```python
USE_LOCAL_API = True  # Читает из папки api/
```
✅ Работает без публикации на GitHub Pages  
✅ Для тестирования

### Удаленный режим
```python
USE_LOCAL_API = False  # Читает с kirillusha.github.io
```
✅ Работает через интернет  
⚠️ Требует публикации на GitHub Pages

## 📚 Документация

- [API_README.md](API_README.md) - Документация API
- [TELEGRAM_BOT_SETUP.md](TELEGRAM_BOT_SETUP.md) - Настройка Telegram бота
- [Примеры использования API](api/index.json)

## 🛠 Технологии

- **Frontend:** HTML, CSS (Tailwind), JavaScript
- **Telegram Bot:** Python, aiogram 3, aiohttp
- **Hosting:** GitHub Pages
- **API:** Static JSON files

## 📄 Структура API

### Цитаты (`/api/quotes.json`)
```json
{
  "quotes": [
    {
      "id": 1,
      "text": "Цитата...",
      "year": 2015
    }
  ]
}
```

### Хронология (`/api/timeline.json`)
```json
{
  "events": [
    {
      "id": 1,
      "year": 1987,
      "title": "Событие",
      "description": "Описание",
      "category": "life"
    }
  ]
}
```

### Картины (`/api/paintings.json`)
```json
{
  "paintings": [
    {
      "id": 1,
      "title": "Название",
      "year": "2015",
      "description": "Описание",
      "colors": ["purple", "blue"],
      "location": "Место",
      "status": "active"
    }
  ]
}
```

## ⚠️ Ограничения GitHub Pages API

✅ **Работает:**
- GET запросы (чтение данных)
- CORS включен автоматически
- Публичный доступ

❌ **Не работает:**
- POST/PUT/DELETE запросы
- Серверная логика
- База данных

## 🔧 Разработка

### Обновление данных API:
1. Отредактируйте файлы в `api/`
2. Закоммитьте изменения
3. Пуш в репозиторий
4. GitHub Pages обновится автоматически (1-2 минуты)

### Тестирование локально:
```bash
# Запустите бота в локальном режиме
USE_LOCAL_API = True
python telegram_bot_example.py
```

## 📞 Поддержка

Если возникли проблемы с ботом:
1. См. [TELEGRAM_BOT_SETUP.md](TELEGRAM_BOT_SETUP.md)
2. Проверьте логи в консоли
3. Используйте команду `/mode` в боте для переключения режима
