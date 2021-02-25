import argparse
import logging
import os
from argparse import Namespace
from multiprocessing import Pool
from parser.pages import ECI, Amazon, Game, MediaMarkt, Worten

from telegram import Telegram
from utils import str2bool

from core.exceptions import ObjectDoesNotExist
from core.settings import Pages

logger = logging.getLogger(__name__)


def init_parser():
    parser = argparse.ArgumentParser(description="AMAZON STOCK")
    parser.add_argument(
        '-c', '--config-file',
        help="Config file",
        default='config/config.yml'
    )

    return parser


def get_object_type(otype: str, config: dict) -> object:
    """
    Object type instance
    :param otype: str Object type
    :param config: dict Specific config for object
    :return object:
    """
    pobj: object = None

    if otype == Pages.AMAZON:
        pobj = Amazon(config=config)

    elif otype == Pages.ECI:
        pobj = ECI(config=config)

    elif otype == Pages.MEDIAMARKT:
        pobj = MediaMarkt(config=config)

    elif otype == Pages.WORTEN:
        pobj = Worten(config=config)

    elif otype == Pages.GAME:
        pobj = Game(config=config)

    if not otype:
        raise ObjectDoesNotExist(f"{otype} does not exist...")

    return pobj


def process_product(args):
    """
    Function for multiprocessing (Pool)
    :param args: dict tlm, msg, web, cfg
    """

    args = Namespace(**args)
    pobj = get_object_type(otype=args.web, config=args.cfg)

    try:
        products = pobj.search_by_id()
        for product in products:
            name: str = product.get('name', product['url'])

            logger.info(f"Product stock: {name}")
            args.tlm.send(f"{args.msg}: {name}\n{product['app']}")

    except Exception as e:
        logger.error(e)


def multiprocessing_main(config: dict):
    """
    Multiprocessing main.
    You can enable with env MULTIPROCESSING
    """
    telegram = Telegram(config=config['telegram'])

    args_list = []
    for web, cfg in config['webs'].items():
        args_list.append(
            dict(
                tlm=telegram,
                msg=config['telegram']['message'],
                web=web,
                cfg=cfg
            )
        )

    pool = Pool(os.cpu_count())
    pool.map(process_product, args_list)
    pool.close()
    pool.join()
