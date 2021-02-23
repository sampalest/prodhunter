import logging
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup
from core.exceptions import ParseRequestException
from core.settings import HEADERS
from utils import get_product

logger = logging.getLogger(__name__)

class Parser(ABC):
    def __init__(self, config: dict):
        self.urls = config
        self.headers = HEADERS
        self.products = []

    def download_html(self, url: str) -> BeautifulSoup:
        """
        This function download html code
        :param url:
        """
        r = requests.get(url, headers=self.headers)

        if not r or r.status_code != requests.codes.ok:
            raise ParseRequestException("Request Exception")

        return BeautifulSoup(r.content, 'html.parser')

    @abstractmethod
    def search_by_id(self) -> list:
        """
        Check if product is available
        :return list:
        """
        raise NotImplementedError('You are invoking a method over an abstract class')
