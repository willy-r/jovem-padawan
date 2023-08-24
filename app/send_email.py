import sys
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app import config


def format_message(sender: str,
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
Olá! 😃
Foram encontradas novas ofertas para o produto que você estava monitorando.
Você pode conferi-las aqui:
    {promos_text}
    """
    html = f"""\
<html lang="pt-br">
  <body>
    <p>Olá! 😃<br>
    Foram encontradas novas ofertas para o produto que você estava monitorando.<br>
    Você pode conferi-las aqui:
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
    message = format_message(sender, receiver, subject, promotions)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as s:
            s.login(sender, password)
            s.sendmail(sender, receiver, message)
    except Exception as err:
        # Break point, can’t continue if email is not sent.
        config.LOGGER.error(f'{err}')
        sys.exit()
