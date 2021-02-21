import argparse

from utils import str2bool


def init_parser():
    parser = argparse.ArgumentParser(description="AMAZON STOCK")
    parser.add_argument(
        '-c', '--config-file',
        help="Config file",
        default='config/config.yml'
    )

    return parser
