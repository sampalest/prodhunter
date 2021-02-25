import os
from enum import Enum

# Settings
DEBUG = bool(os.environ.get('DEBUG', False))
MULTIPROCESSING = bool(os.environ.get('MULTIPROCESSING', False))
TELEGRAM_SEND = bool(os.environ.get('TELEGRAM_SEND', False))

# Schedule Time (minutes)
SCHEDULE_TIME = os.environ.get('SCHEDULE_TIME', 1)

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
