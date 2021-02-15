import requests
from bs4 import BeautifulSoup


class Parser():
    def __init__(self):
        self.url = "https://www.amazon.es/Estación-recarga-DualSense-PlayStation-5/dp/B08H97WTBL"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    def download_html(self):
        r = requests.get(self.url, )