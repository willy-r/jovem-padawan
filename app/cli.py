import argparse
from getpass import getpass
from dataclasses import dataclass

from app import config


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Monitor and send an email of promotions on Hardmob site',
    )
    parser.add_argument('product',
                        help='product name for monitor')

    parser.add_argument('-d',
                        '--delay',
                        type=int,
                        action='store',
                        choices=[2, 5, 10, 20],
                        default=5,
                        help='delay between the monitor (default is 5 minutes)')

    parser.add_argument('-e',
                        '--email',
                        action='store',
                        default=config.EMAIL_USERNAME,
                        help='valid gmail account (prompt if not passed)')

    parser.add_argument('-p',
                        '--password',
                        action='store',
                        default=config.EMAIL_PASSWORD,
                        help='email’s password (prompt if not passed)')
    return parser.parse_args()


args = get_args()


@dataclass
class ArgumentsHandler:
    product: str = args.product.capitalize()
    email: str = args.email or input('? E-mail: ')
    sender_email: str = email
    receiver_email: str = email.replace('@gmail.com', '+receiver@gmail.com')
    password: str = args.password or getpass('? Senha do e-mail: ')
    delay_sec: int = args.delay * 60
