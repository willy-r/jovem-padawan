import argparse
from getpass import getpass
from dataclasses import dataclass


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Monitor and send an email of promotions on Hardmob site',
    )
    parser.add_argument('product',
                        help='product name for monitor')

    parser.add_argument('email',
                        help='valid gmail account for receive/send promotions')

    parser.add_argument('-d',
                        '--delay',
                        type=int,
                        action='store',
                        choices=[2, 5, 10, 20],
                        default=5,
                        help='delay between the monitor (default is 5 minutes')

    parser.add_argument('-p',
                        '--password',
                        action='store',
                        help='email’s password (prompt if not passed)')
    return parser.parse_args()


args = get_args()


@dataclass
class ArgumentsHandler:
    product: str = args.product.capitalize()
    email: str = args.email
    sender_email: str = email
    receiver_email: str = email.replace('@gmail.com', '+receiver@gmail.com')
    password: str = args.password or getpass('? Senha do E-mail: ')
    delay_sec: int = args.delay * 60
