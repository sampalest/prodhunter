import logging

import requests

from core import init_parser
from telegram import Telegram
from utils import get_config

logger = logging.getLogger(__name__)


# def telegram_bot_sendtext(bot_message):
#     bot_token = '1640016697:AAFkrEGAzRWwkvKjZgFDHB8P_AvlJGVRdKg'
#     bot_chatID = '215646543'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

#     response = requests.get(send_text)

#     return response.json()


# def report():
#     my_message = "Message"
#     telegram_bot_sendtext(my_message)


if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    config = get_config(path=args.config_file)

    telegram = Telegram(config=config['telegram'])

    logger.info("Sending message")
    try:
        telegram.send("Telegram Object Send")
    except Exception as e:
        logger.error(e)
