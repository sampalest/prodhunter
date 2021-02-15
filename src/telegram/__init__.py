import requests
from core.exceptions import ResponseErrorException

class Telegram:
    def __init__(self, config: dict):
        self.token = config['token']
        self.chat_id = config['chatID']
        self.api = self._build_api()

    def _build_api(self) -> str:
        return 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}'.format(self.token, self.chat_id)

    def send(self, message: str) -> dict:
        text_url = f"{self.api}'&parse_mode=Markdown&text={message}"
        response = requests.get(text_url)

        if response.status_code != requests.codes.ok:
            raise ResponseErrorException("Telegram API Error")

        return response.json()
