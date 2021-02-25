import logging

from core.exceptions import ParseRequestException
from utils import get_product

from parser import Parser

logger = logging.getLogger(__name__)


class Amazon(Parser):
    def __init__(self, config):
        super(Amazon, self).__init__(config)
        self.ids = ['buy-now-button', 'add-to-cart-button']

    def search_by_id(self):
        result = None

        for item in self.urls:
            url = item['url']
            name = item.get('name', '')
            app = get_product(url)

            logger.info(f"[{self.__class__.__name__}] Parsing... {name}")

            try:
                html = self.download_html(url)

            except ParseRequestException:
                logger.error(
                    f"[{self.__class__.__name__}] Request error for name {name}")
                continue

            for id in self.ids:
                result = html.find_all(id=id)

            if result:
                self.products.append(dict(url=url, name=name, app=app))

        return self.products


class ECI(Parser):
    def __init__(self, config):
        super(ECI, self).__init__(config)
        self.class_ = ['js-add-to-cart', 'oneclick']

    def search_by_id(self):
        result = None

        for item in self.urls:
            url = item['url']
            name = item.get('name', '')

            logger.info(f"[{self.__class__.__name__}] Parsing... {name}")

            try:
                html = self.download_html(url)

            except ParseRequestException:
                logger.error(
                    f"[{self.__class__.__name__}] Request error for name {name}")
                continue

            for class_ in self.class_:
                # In this case search by class name
                result = html.find_all('button', class_)

            if result:
                self.products.append(dict(url=url, name=name, app=url))

        return self.products


class MediaMarkt(Parser):
    def __init__(self, config):
        super(MediaMarkt, self).__init__(config)
        self.ids = ['pdp-add-to-cart-button']

    def search_by_id(self):
        result = None

        for item in self.urls:
            url = item['url']
            name = item.get('name', '')
            clss = self.__class__.__name__.lower()
            app = get_product(url, class_=clss)

            logger.info(f"[{self.__class__.__name__}] Parsing... {name}")

            try:
                html = self.download_html(url)

            except ParseRequestException:
                logger.error(
                    f"[{self.__class__.__name__}] Request error for name {name}")
                continue

            for id in self.ids:
                result = html.find_all(id=id)

            if result:
                self.products.append(dict(url=url, name=name, app=app))

        return self.products


class Game(Parser):
    def __init__(self, config):
        super(Game, self).__init__(config)
        self.class_ = ['buy-button']

    def search_by_id(self):
        result = None

        for item in self.urls:
            url = item['url']
            name = item.get('name', '')

            logger.info(f"[{self.__class__.__name__}] Parsing... {name}")

            try:
                html = self.download_html(url)

            except ParseRequestException:
                logger.error(
                    f"[{self.__class__.__name__}] Request error for name {name}")
                continue

            for class_ in self.class_:
                result = html.find_all('a', class_)

            if result:
                self.products.append(dict(url=url, name=name, app=url))

        return self.products


class Worten(Parser):
    def __init__(self, config):
        super(Worten, self).__init__(config)
        self.class_ = ['qa-product-options__add-cart-linkto']

    def search_by_id(self):
        result = None

        for item in self.urls:
            url = item['url']
            name = item.get('name', '')

            logger.info(f"[{self.__class__.__name__}] Parsing... {name}")

            try:
                html = self.download_html(url)

            except ParseRequestException:
                logger.error(
                    f"[{self.__class__.__name__}] Request error for name {name}")
                continue

            for class_ in self.class_:
                result = html.find_all('button', class_)

            if result:
                self.products.append(dict(url=url, name=name, app=url))

        return self.products
