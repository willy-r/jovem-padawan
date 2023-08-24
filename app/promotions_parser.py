import re
import sys

import bs4
import requests

from app import config

SENT = {}


def get_target_site() -> bytes:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        }
        r = requests.get(config.TARGET_URL.geturl(), headers=headers, timeout=2)
        r.raise_for_status()
    except Exception as err:
        # Just stop the whole process, can’t continue without data.
        config.LOGGER.error(f'{err}')
        sys.exit()
    return r.content


def promotions_to_send(promotions: list[bs4.element.Tag]) -> list[tuple[str]]:
    to_send = []
    for promo in promotions:
        p_url = config.TARGET_URL._replace(path=promo['href']).geturl()
        p_text = promo.get_text(strip=True)

        # Verify for promotions that was already sent.
        # (There's a bug on this aproach, fix later.)
        if p_text in SENT:
            continue

        SENT.setdefault(p_text)
        to_send.append((p_text, p_url))
    return to_send


def parse_promotions(search_for: str) -> list[tuple[str]]:
    content = get_target_site()
    soup = bs4.BeautifulSoup(content, 'html.parser')

    # This will find all the promotions on the first page
    # with the search_for (ignore case sensitive) specified.
    # (Can be anything.)
    promotions = soup.find_all(
        'a',
        class_='title',
        string=re.compile(search_for, re.IGNORECASE),
    )
    return promotions_to_send(promotions)
