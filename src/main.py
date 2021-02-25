import logging
import os
import time

import requests
import schedule

from core import init_parser, multiprocessing_main, process_product
from core.settings import DEBUG, MULTIPROCESSING, SCHEDULE_TIME
from telegram import Telegram
from utils import get_config

logger = logging.getLogger(__name__)

def main():
    parser = init_parser()
    args = parser.parse_args()
    config = get_config(path=args.config_file)

    logger.info(f"MULTIPROCESSING is {MULTIPROCESSING}")

    if MULTIPROCESSING:
        multiprocessing_main(config=config)

    else:
        telegram = Telegram(config=config['telegram'])
        for web, cfg in config['webs'].items():
            process_product({
                'tlm': telegram,
                'msg': config['telegram']['message'],
                'web': web,
                'cfg': cfg
            })

if __name__ == "__main__":
    logger.debug(f"Debug is {DEBUG}")

    if not DEBUG:
        schedule.every(SCHEDULE_TIME).minutes.do(main)
        while True:
            schedule.run_pending()
            time.sleep(schedule.idle_seconds())
    else:
        main()
