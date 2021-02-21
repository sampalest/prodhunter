import logging

import requests
from bs4 import BeautifulSoup
from core.settings import RANDOM_IP
from core.exceptions import ParseRequestException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from utils import get_product

logger = logging.getLogger(__name__)

class Parser():
    def __init__(self, config):
        self.urls = config['urls']
        self.headers = config['header']

    def _download_html(self, url) -> BeautifulSoup:
        r = requests.get(url, headers=self.headers)
        
        if not r or r.status_code != requests.codes.ok:
            raise ParseRequestException("Request Exception")

        return BeautifulSoup(r.content, 'html.parser')      

    def search_by_id(self, ids: list = ['buy-now-button', 'add-to-cart-button']) -> bool:
        """
        Check if product is available
        :param ids: Search for html ids
        :return: bool
        """
        result = None
        products: list = []

        for item in self.urls:
            url = item['url']
            name = item.get('name', '')
            app = get_product(url)

            logger.info(f"Parsing... {name}")
            
            try:
                html = self._download_html(url)
            
            except ParseRequestException:
                logger.error(f"[Parse] Request error for name {name}")
                continue

            for id in ids:
                result = html.find_all(id=id)

            if result:
                products.append(dict(url=url, name=name, app=app))

        return products
