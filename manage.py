import requests
import telegram
from environs import Env


def send_feedback(attempt, bot, chat_id):
    lesson_name = attempt['lesson_title']
    lesson_url = attempt['lesson_url']
    verdict = attempt['is_negative']
    result = "не принята" if verdict else "принята"
    message = (
        f"Урок: {lesson_name}\n"
        f"Результат проверки: {result}\n"
        f"Ссылка на урок: {lesson_url}"
    )
    bot.send_message(chat_id=chat_id, text=message)


def main():
    env = Env()
    env.read_env()

    tg_token = env.str("TG_TOKEN")
    api_devman_token = env.str("API_DEVMAN_TOKEN")

    chat_id = input('Введите чат ID, куда будут присылать уведомления. Пример: "-1001234567890": ')
    bot = telegram.Bot(token=tg_token)

    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': api_devman_token}
    last_timestamp = None

    while True:
        try:
            params = {}
            if last_timestamp is not None:
                params['timestamp'] = last_timestamp

            response = requests.get(url, headers=headers, params=params, timeout=90)
            response.raise_for_status()
            response_json = response.json()

            if 'new_attempts' in response_json:
                for attempt in response_json['new_attempts']:
                    last_timestamp = attempt['timestamp']
                    send_feedback(attempt, bot, chat_id)

        except requests.exceptions.ReadTimeout:
            print('ReadTimeout: Проектов нет.')
        except requests.exceptions.ConnectionError:
            print('ConnectionError: Повторное подключение...')
            continue


if __name__ == "__main__":
    main()
