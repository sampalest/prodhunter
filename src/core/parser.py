import requests
from bs4 import BeautifulSoup


class Parser():
    def __init__(self, config):
        self.url = config['url']
        self.headers = config['header']

    def _download_html(self) -> BeautifulSoup:
        r = requests.get(self.url, headers=self.headers)
        return BeautifulSoup(r.content, 'html.parser')

    def search_by_id(self, ids: list = ['buy-now-button', 'add-to-cart-button']) -> bool:
        """
        Check if product is available
        :param ids: Search for html ids
        :return: bool
        """
        result = None
        html = self._download_html()

        for id in ids:
            result = html.find_all(id=id)

        return True if result else False
