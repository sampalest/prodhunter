import requests

from ruamel.yaml import YAML


def get_config(path: str) -> dict:
    with open(path, 'r') as config_file:
        yaml = YAML()
        cdata = yaml.load(config_file)

    return cdata
