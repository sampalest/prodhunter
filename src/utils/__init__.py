import argparse
import logging
import re

import requests
from ruamel.yaml import YAML

from core.settings import AMAZON_ES, Pages
from core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_config(path: str) -> dict:
    """
    Read config from YAML
    :return dict:
    """
    with open(path, 'r') as config_file:
        yaml = YAML()
        cdata = yaml.load(config_file)

    return cdata


def get_product(url: str, class_: str = 'amazon') -> str:
    """
    Get product ID
    :param url:
    :return str:
    """
    app_dir: str = url
    try:
        if class_ == Pages.AMAZON:
            dp = re.search('(dp/.*/|dp/.*)', url)
            app_dir = f'{AMAZON_ES}/{dp.group(0)}'

        elif class_ == Pages.MEDIAMARKT:
            app_dir = url.replace('_', '')

    except Exception as e:
        logger.error(e)

    finally:
        # Remove final slash
        if app_dir[-1] == '/':
            app_dir = app_dir[:-1]

    return app_dir
