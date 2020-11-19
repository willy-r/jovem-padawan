import logging
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format='(%(asctime)s) - %(name)s: %(levelname)s: %(message)s',
    datefmt='%H:%M',
)
LOGGER = logging.getLogger('padawan.py')

URL = urlparse('https://www.hardmob.com.br/forums/407-Promocoes')
