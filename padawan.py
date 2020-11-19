from time import sleep

from padawan.config import LOGGER, URL
from padawan.send_email import send_email
from padawan.cli import ArgumentsHandler as args
from padawan.promotions_parser import parse_promotions


def main() -> None:
    prod = args.product
    subject = f'Há novas ofertas disponíveis para "{prod}"'

    while True:
        LOGGER.info(f'Procurando por ofertas para "{prod}" em {URL.geturl()}')

        promos = parse_promotions(prod)
        if not promos:
            LOGGER.info(f'Não há novas ofertas para "{prod}" no momento\n')
        else:
            LOGGER.info(f'Novas ofertas encontradas para "{prod}"')
            send_email(
                args.sender_email,
                args.receiver_email,
                args.password,
                subject,
                promos,
            )
            LOGGER.info(f'Enviado e-mail com as ofertas para {args.email}\n')
        sleep(args.delay_sec)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        LOGGER.info('Finalizando o processo...')
