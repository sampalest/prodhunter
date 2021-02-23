import argparse

from utils import str2bool
from parser.pages import Amazon, ECI, MediaMarkt
from core.settings import Pages
from core.exceptions import ObjectDoesNotExist


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

    if not otype:
        raise ObjectDoesNotExist(f"{otype} does not exist...")

    return pobj
