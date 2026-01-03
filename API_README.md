# API для Telegram Бота

Этот API позволяет Telegram боту получать данные о Александре Невском.

## 🌐 Base URL
```
https://kirillusha.github.io/api
```

## 📡 Endpoints

### 1. Все эндпоинты
**GET** `/api/index.json`
- Список всех доступных эндпоинтов

### 2. Цитаты
**GET** `/api/quotes.json`
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

### 3. Хронология
**GET** `/api/timeline.json`
```json
{
  "events": [
    {
      "id": 1,
      "year": 1987,
      "title": "Название",
      "description": "Описание",
      "category": "life"
    }
  ]
}
```

### 4. Картины
**GET** `/api/paintings.json`
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

## 🤖 Использование в Telegram боте

### Установка зависимостей
```bash
pip install python-telegram-bot requests
```

### Запуск
1. Создайте бота через @BotFather в Telegram
2. Получите токен
3. Замените `YOUR_BOT_TOKEN` в `telegram_bot_example.py`
4. Запустите: `python telegram_bot_example.py`

### Команды бота
- `/start` - Приветствие
- `/quote` - Случайная цитата
- `/quotes` - Все цитаты
- `/timeline` - Хронология жизни
- `/paintings` - Список картин
- `/painting 1` - Детали картины #1

## ⚠️ Ограничения

✅ **Работает:**
- GET запросы (чтение данных)
- Публичный доступ без авторизации
- CORS включен по умолчанию в GitHub Pages

❌ **Не работает:**
- POST/PUT/DELETE запросы (запись данных)
- База данных
- Серверная логика

## 🔄 Обновление данных

Для обновления данных API нужно:
1. Отредактировать JSON файлы в папке `/api/`
2. Закоммитить изменения
3. GitHub Pages автоматически обновит сайт

## 💡 Дополнительные возможности

### Использование GitHub API как база данных
Вы можете использовать GitHub Issues/Gists для хранения динамических данных:

```python
# Пример чтения данных из GitHub Gist
import requests

gist_id = "YOUR_GIST_ID"
response = requests.get(f"https://api.github.com/gists/{gist_id}")
data = response.json()
```

### CORS
GitHub Pages автоматически поддерживает CORS, поэтому запросы из Telegram бота будут работать без проблем.
