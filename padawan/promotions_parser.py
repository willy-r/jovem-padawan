import re
import sys

import bs4
import requests

from .config import LOGGER, URL

SENT = {}


def _find() -> bytes:
    try:
        r = requests.get(URL.geturl(), timeout=2)
        r.raise_for_status()
    except Exception as err:
        # Just stop the whole process, can’t continue without data.
        LOGGER.error(f'{err}')
        sys.exit()
    return r.content


def _to_send(promotions: list[bs4.element.Tag]) -> list[tuple[str]]:
    to_send = []
    for promo in promotions:
        p_url = URL._replace(path=promo['href']).geturl()
        p_text = promo.get_text(strip=True)

        # Verify for promotions that was already sent.
        # (There's a bug on this aproach, fix later.)
        if p_text in SENT:
            continue

        SENT[p_text] = p_url
        to_send.append((p_text, p_url))
    return to_send


def parse_promotions(search_for: str) -> list[tuple[str]]:
    content = _find()
    soup = bs4.BeautifulSoup(content, 'html.parser')

    # This will find all the promotions on the first page
    # with the search_for (ignore case sensitive) specified.
    # (Can be anything.)
    promotions = soup.find_all(
        'a',
        class_='title',
        string=re.compile(search_for, re.IGNORECASE),
    )
    return _to_send(promotions)
