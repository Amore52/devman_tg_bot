# Telegram Bot для уведомлений о проверке уроков

Этот скрипт использует API Devman и Telegram Bot API для отправки уведомлений о проверке уроков. Когда появляется новый результат проверки, бот отправляет сообщение с информацией о уроке, его статусе (принята или не принята) и ссылкой на урок.

## Требования

1. Python 3.8 или выше.
2. Установленные библиотеки:
- `requests 2.31.0` 
- `python-telegram-bot 13.15` 
- `urllib3 1.26.5`

## Настройка проекта

### 1. Создание виртуального окружения

Рекомендуется создать виртуальное окружение для изоляции зависимостей проекта.

1. **Создайте виртуальное окружение**:

    ```
    python -m venv .venv
2. **Активируйте виртуальное окружение:**
    ```
   .venv\Scripts\activate
    ```
### 2. Установка зависимостей
    
```
pip install -r requirements.txt
```

### 3. Создание файла .env

`TG_TOKEN` - Токен для вашего бота Telegram, который вы получаете, создав бота через BotFather. \
`API_DEVMAN_TOKEN` - Токен для доступа к API Devman, который вы получите, зарегистрировавшись на платформе Devman.

### 4. Запуск скрипта

```
python manage.py
```
После запуска программа предложит ввести вам ID чата, в который будет присылать уведомления.
ID чата всегда начинается с `-100`:
```
Введите чат ID, куда будут присылать уведомления. Пример: "-1001234567890": 

```

### 5. Пример уведомления:
Если урок называется "Как сделать бота", результат проверки не принят, и ссылка на урок: `https://example.com/lesson/1`, то бот отправит:
```
Урок: Как сделать бота
Результат проверки: не принята
Ссылка на урок: https://example.com/lesson/1
```