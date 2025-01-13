import requests
import telegram
import time
from environs import Env


def send_feedback(attempt, bot, chat_id):
    lesson_name = attempt['lesson_title']
    lesson_url = attempt['lesson_url']
    verdict = attempt['is_negative']
    final_verdict = "не принята" if verdict else "принята"
    message = (
        f"Урок: {lesson_name}\n"
        f"Результат проверки: {final_verdict}\n"
        f"Ссылка на урок: {lesson_url}"
    )
    bot.send_message(chat_id=chat_id, text=message)


def main():
    env = Env()
    env.read_env()

    tg_token = env.str("TG_TOKEN")
    api_devman_token = env.str("API_DEVMAN_TOKEN")
    chat_id = env.str("CHAT_ID", default="-1001234567890")
    bot = telegram.Bot(token=tg_token)

    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': api_devman_token}
    last_timestamp = None
    while True:
        try:
            params = {}
            if last_timestamp:
                params['timestamp'] = last_timestamp

            response = requests.get(url, headers=headers, params=params, timeout=90)
            response.raise_for_status()
            response_content = response.json()

            if 'new_attempts' in response_content:
                for attempt in response_content['new_attempts']:
                    last_timestamp = attempt['timestamp']
                    send_feedback(attempt, bot, chat_id)

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            print('ConnectionError: Повторное подключение...')
            time.sleep(60)
            continue


if __name__ == "__main__":
    main()
