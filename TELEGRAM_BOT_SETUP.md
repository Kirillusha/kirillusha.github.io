# 🤖 Telegram Bot для API на GitHub Pages

## 📋 Оглавление
- [Быстрый старт](#быстрый-старт)
- [Режимы работы](#режимы-работы)
- [Публикация на GitHub Pages](#публикация-на-github-pages)
- [Устранение проблем](#устранение-проблем)

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
pip install aiogram aiohttp
```

### 2. Создание бота
1. Откройте Telegram
2. Найдите @BotFather
3. Отправьте команду `/newbot`
4. Следуйте инструкциям
5. Скопируйте токен

### 3. Запуск бота

**Замените токен в файле:**
```python
bot = Bot(token="YOUR_BOT_TOKEN")  # Вставьте свой токен
```

**Запустите:**
```bash
python telegram_bot_example.py
```

## 🔄 Режимы работы

Бот поддерживает два режима:

### 📁 Локальный режим (по умолчанию)
```python
USE_LOCAL_API = True
```
- ✅ Работает сразу после скачивания
- ✅ Не требует публикации на GitHub Pages
- ✅ Читает данные из папки `/api/`
- ⚠️ Для тестирования

### 🌐 Удаленный режим
```python
USE_LOCAL_API = False
```
- ✅ Работает через интернет
- ✅ Доступ из любого места
- ⚠️ Требует публикации на GitHub Pages

**Переключение режима в боте:**
```
/mode - Переключить между локальным и удаленным API
```

## 📤 Публикация на GitHub Pages

### Способ 1: Через веб-интерфейс GitHub

1. **Откройте ваш репозиторий на GitHub**
   ```
   https://github.com/kirillusha/kirillusha.github.io
   ```

2. **Перейдите в Settings (Настройки)**
   - Нажмите на вкладку "Settings"

3. **Найдите раздел "Pages"**
   - В левом меню выберите "Pages"

4. **Настройте источник**
   - Source: Deploy from a branch
   - Branch: `cursor/github-pages-api-possibility-24b7` (или `main`)
   - Folder: `/ (root)`
   - Нажмите "Save"

5. **Дождитесь публикации**
   - GitHub Pages начнет деплой (1-2 минуты)
   - После завершения появится ссылка:
   ```
   Your site is live at https://kirillusha.github.io
   ```

6. **Проверьте API**
   Откройте в браузере:
   - https://kirillusha.github.io/api/quotes.json
   - https://kirillusha.github.io/api/timeline.json
   - https://kirillusha.github.io/api/paintings.json

### Способ 2: Через командную строку

```bash
# 1. Коммит изменений (если еще не сделано)
git add api/
git commit -m "Add API endpoints"

# 2. Пуш в репозиторий
git push origin cursor/github-pages-api-possibility-24b7

# 3. Настроить GitHub Pages через веб-интерфейс (см. выше)
```

### Способ 3: Через GitHub CLI

```bash
# Включить GitHub Pages
gh api repos/kirillusha/kirillusha.github.io/pages \
  -X POST \
  -F source[branch]=cursor/github-pages-api-possibility-24b7 \
  -F source[path]=/
```

## ✅ Проверка работы API

### 1. Проверка через браузер
Откройте URL и убедитесь, что видите JSON:
```
https://kirillusha.github.io/api/quotes.json
```

Должно вернуть:
```json
{
  "quotes": [
    {
      "id": 1,
      "text": "Я не рисую то, что вижу...",
      "year": 2015
    }
  ]
}
```

### 2. Проверка через curl
```bash
curl https://kirillusha.github.io/api/quotes.json
```

### 3. Проверка в боте
После публикации:
1. Откройте `telegram_bot_example.py`
2. Измените `USE_LOCAL_API = False`
3. Перезапустите бота
4. Отправьте команду `/quote`

## ❗ Устранение проблем

### Проблема: "Не удалось получить данные"

**Локальный режим (USE_LOCAL_API = True):**
```bash
# Проверьте наличие файлов
ls -la api/
# Должны быть: quotes.json, timeline.json, paintings.json
```

**Удаленный режим (USE_LOCAL_API = False):**
1. Проверьте, что сайт опубликован на GitHub Pages
2. Откройте в браузере: https://kirillusha.github.io/api/quotes.json
3. Если 404 - сайт не опубликован или неправильный путь
4. Если JSON отображается - проблема в боте

### Проблема: 404 Not Found

**Причины:**
- GitHub Pages не настроен
- Неправильная ветка выбрана
- Файлы не закоммичены

**Решение:**
```bash
# 1. Проверьте текущую ветку
git branch

# 2. Убедитесь, что файлы закоммичены
git status

# 3. Если есть изменения - закоммитьте
git add api/
git commit -m "Add API files"
git push
```

### Проблема: CORS ошибка

GitHub Pages **автоматически** поддерживает CORS, но если возникают проблемы:

**Решение:**
- Убедитесь, что используете `https://` (не `http://`)
- Проверьте URL: должен быть `kirillusha.github.io`, не `github.io/kirillusha`

### Проблема: Данные устаревшие

GitHub Pages кэширует файлы. Для обновления:

1. **Подождите 1-2 минуты** после пуша
2. **Очистите кэш браузера** (Ctrl+F5)
3. **Добавьте параметр в URL:**
   ```
   https://kirillusha.github.io/api/quotes.json?v=2
   ```

## 📊 Структура проекта

```
/workspace/
├── api/                           # API эндпоинты
│   ├── index.json                 # Список всех эндпоинтов
│   ├── quotes.json                # Цитаты
│   ├── timeline.json              # Хронология
│   └── paintings.json             # Картины
├── telegram_bot_example.py        # Telegram бот
├── requirements.txt               # Зависимости Python
├── API_README.md                  # Эта документация
└── index.html                     # Сайт
```

## 🎯 Команды бота

После запуска бота доступны команды:

| Команда | Описание |
|---------|----------|
| `/start` | Приветствие и список команд |
| `/mode` | Переключить локальный/удаленный режим |
| `/quote` | Случайная цитата |
| `/quotes` | Все цитаты |
| `/timeline` | Хронология жизни |
| `/paintings` | Список картин |
| `/painting 1` | Детали картины #1 |

## 💡 Дополнительно

### Обновление данных API

**Локально:**
1. Отредактируйте файл в `/api/`
2. Сохраните изменения
3. Перезапустите бота (если нужно)

**На GitHub Pages:**
1. Отредактируйте файл в `/api/`
2. Закоммитьте:
   ```bash
   git add api/
   git commit -m "Update API data"
   git push
   ```
3. Подождите 1-2 минуты для деплоя

### Добавление нового эндпоинта

1. Создайте новый JSON файл в `/api/`:
   ```bash
   echo '{"data": []}' > api/new_endpoint.json
   ```

2. Добавьте функцию в бота:
   ```python
   async def get_new_data():
       if USE_LOCAL_API:
           data = await get_data_from_file("new_endpoint.json")
       else:
           data = await get_data_from_url(f"{API_BASE_URL}/new_endpoint.json")
       return data.get("data", []) if data else []
   ```

3. Добавьте команду:
   ```python
   @router.message(Command("newcmd"))
   async def cmd_new(message: Message):
       data = await get_new_data()
       await message.answer(str(data))
   ```

## 🔒 Безопасность

⚠️ **ВАЖНО:**
- Никогда не коммитьте токен бота в Git
- Используйте переменные окружения:
  ```python
  import os
  TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
  ```
- Для продакшена используйте `.env` файл

## 📞 Поддержка

Если возникли проблемы:
1. Проверьте логи бота (в консоли)
2. Проверьте доступность API в браузере
3. Используйте команду `/mode` для переключения режима
4. Убедитесь, что GitHub Pages настроен правильно
