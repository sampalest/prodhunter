import logging

import requests
import time

import schedule
from core import init_parser
from core.parser import Parser
from telegram import Telegram
from utils import get_config

logger = logging.getLogger(__name__)

def main():
    parser = init_parser()
    args = parser.parse_args()
    config = get_config(path=args.config_file)

    telegram = Telegram(config=config['telegram'])
    pobj = Parser(config=config['amazon'])

    try:
        logger.info("Parsing web...")

        stock = pobj.search_by_id()
        if stock:
            logger.info("Sending alert")
            telegram.send(f"{config['telegram']['message']}: {config['amazon'].get('url_mobile', config['amazon']['url'])}")

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    schedule.every(1).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(schedule.idle_seconds())
