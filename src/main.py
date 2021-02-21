import logging
import os
import time

import requests
import schedule

from core import init_parser
from core.parser import Parser
from telegram import Telegram
from utils import get_config

logger = logging.getLogger(__name__)
DEBUG = os.environ.get('DEBUG', False)

def main():
    parser = init_parser()
    args = parser.parse_args()
    config = get_config(path=args.config_file)

    telegram = Telegram(config=config['telegram'])
    pobj = Parser(config=config['amazon'])

    try:
        logger.info("Executing...")
        products = pobj.search_by_id()
        for product in products:
            msg: str = config['telegram']['message']
            name: str = product.get('name', product['url'])

            logger.info(f"Product stock: {name}")
            # telegram.send(f"{msg}: {name}\n{product['app']}")

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    logger.debug(f"Debug is {DEBUG}")

    if not DEBUG:
        schedule.every(1).minutes.do(main)
        while True:
            schedule.run_pending()
            time.sleep(schedule.idle_seconds())
    else:
        main()
