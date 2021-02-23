import os
from enum import Enum

# Constants
AMAZON_ES = 'https://www.amazon.es'
TELEGRAM_API_MESSAGE = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s'

# Header
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

# Pages type
class Pages(str, Enum):
    AMAZON = 'amazon'
    CARREFOUR = 'carrefour'
    MEDIAMARKT = 'mediamarkt'
    WORTEN = 'worten'
    ECI = 'eci'
