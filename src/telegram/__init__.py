import logging

import requests

from core.settings import TELEGRAM_API_MESSAGE, TELEGRAM_SEND
from core.exceptions import ResponseErrorException

logger = logging.getLogger(__name__)


class Telegram:
    def __init__(self, config: dict):
        self.api = TELEGRAM_API_MESSAGE % (config['token'], config['chatID'])

    def send(self, message: str) -> dict:
        if not TELEGRAM_SEND:
            return {}

        logger.info("Sending message...")
        text_url = f"{self.api}'&parse_mode=Markdown&text={message}"
        response = requests.get(text_url)

        if response.status_code != requests.codes.ok:
            raise ResponseErrorException("Telegram API Error")

        return response.json()
