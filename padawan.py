import re
import sys
import ssl
import smtplib
import argparse
from time import sleep
from getpass import getpass
from urllib.parse import urlparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import bs4
import requests

URL = urlparse('https://www.hardmob.com.br/forums/407-Promocoes')
SENT = {}


def _find() -> bytes:
    try:
        r = requests.get(URL.geturl(), timeout=2)
        r.raise_for_status()
    except Exception as err:
        # Just stop the whole process.
        sys.exit(f'{sys.argv[0]}: ERROR: {err}')
    return r.content


def _to_send(promotions: list[bs4.element.Tag]) -> list[tuple[str]]:
    to_send = []
    for promo in promotions:
        p_url = URL._replace(path=promo['href']).geturl()
        p_text = promo.get_text(strip=True)
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
    promotions = soup.find_all(
        'a',
        class_='title',
        string=re.compile(search_for, re.IGNORECASE),
    )
    return _to_send(promotions)


def _format_message(sender: str,
                    receiver: str,
                    subject: str,
                    promotions: list[tuple[str]]) -> str:
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    promos_text = '\n'.join([(f'{p[0]} -> {p[1]}')
                             for p in promotions])
    promos_html = '\n'.join([(f'<li><a href="{p[1]}">{p[0]}</a></li>')
                             for p in promotions])

    text = f"""\
Hello! 😃
There's some new promotions available that you can check here:
    {promos_text}
    """
    html = f"""\
<html lang='en'>
  <body>
    <p>Hello! 😃<br>
    There's some new promotions available that you can check here:
    <ul>
      {promos_html}
    </ul>
    </p>
  </body>
</html>
    """
    # Turn these into plain/html MIMEText objects.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Add HTML/plain-text parts to MIMEMultipart message.
    # The email client will try to render the last part first.
    message.attach(part1)
    message.attach(part2)

    return message.as_string()


def send_email(sender: str,
               receiver: str,
               password: str,
               subject: str,
               promotions: list[tuple[str]]) -> None:
    message = _format_message(sender, receiver, subject, promotions)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as s:
            s.login(sender, password)
            s.sendmail(sender, receiver, message)
    except Exception as err:
        # Another break point.
        sys.exit(f'{sys.argv[0]}: ERROR: {err}')


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='padawan',
        description='Find and send an email of promotions on Hardmob site',
    )
    parser.add_argument('product',
                        help='product name for find promotions')

    parser.add_argument('email',
                        help='valid email for receiving the promotions')

    parser.add_argument('-t',
                        '--time',
                        type=int,
                        action='store',
                        choices=[2, 5, 10, 20],
                        default=5,
                        help=('time for monitoring the '
                              'promotions (default 5 minutes)'))

    parser.add_argument('-p',
                        '--password',
                        action='store',
                        help='email’s password')

    return parser.parse_args()


def main() -> None:
    args = get_args()
    product = args.product.capitalize()
    email = args.email
    sender_email = email
    receiver_email = email.replace('@gmail.com', '+receiver@gmail.com')
    password = args.password
    if password is None:
        password = getpass('? Email’s password: ')

    subject = f'New promotions found for "{product}"'
    delay_sec = args.time * 60

    while True:
        print(f'\n{sys.argv[0]}: INFO: Monitoring for '
              f'"{product}" in {URL.geturl()}')

        promos = parse_promotions(product)
        if not promos:
            print(f'{sys.argv[0]}: INFO: No promotions found for "{product}"')
        else:
            print(f'{sys.argv[0]}: INFO: New promotions found for "{product}"')
            send_email(sender_email, receiver_email, password, subject, promos)
            print(f'{sys.argv[0]}: INFO: Sending email to {email}...')
        sleep(delay_sec)


if __name__ == '__main__':
    main()
