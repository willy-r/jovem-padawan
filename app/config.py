import os
import logging
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format='(%(asctime)s) - %(name)s: %(levelname)s: %(message)s',
    datefmt='%H:%M',
)
LOGGER = logging.getLogger('jovem-padawan')

TARGET_URL = urlparse('https://www.hardmob.com.br/forums/407-Promocoes')

EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
