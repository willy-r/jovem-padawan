from time import sleep

from dotenv import load_dotenv

load_dotenv()

from app import config
from app.send_email import send_email
from app.cli import ArgumentsHandler as args
from app.promotions_parser import parse_promotions


def main() -> None:
    prod = args.product
    subject = f'Há novas ofertas disponíveis para "{prod}"'

    while True:
        config.LOGGER.info(f'Procurando por ofertas para "{prod}" em {config.TARGET_URL.geturl()}')

        promos = parse_promotions(prod)
        if not promos:
            config.LOGGER.info(f'Não há novas ofertas para "{prod}" no momento\n')
        else:
            config.LOGGER.info(f'Novas ofertas encontradas para "{prod}"')
            send_email(
                args.sender_email,
                args.receiver_email,
                args.password,
                subject,
                promos,
            )
            config.LOGGER.info(f'Enviado e-mail com as ofertas para {args.email}\n')
        sleep(args.delay_sec)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        config.LOGGER.info('Finalizando o processo...')
