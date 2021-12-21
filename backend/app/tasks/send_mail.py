from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from typing import Optional

from app.config import MAIL_USERNAME, MAIL_PASSWORD, MAIL_PORT, MAIL_SERVER
from app.worker import worker


@worker.task(name="send_email")
def send_mail(recipient: str, subject: str, body: str, html: Optional[str] = None) -> None:
    """
    Sends an email to the given recipient.

    :param recipient: The recipient of the email.
    :param subject: The subject of the email.
    :param body: The body of the email.
    :param html: The HTML content of the email.
    """
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = MAIL_USERNAME
    message["To"] = recipient
    message.attach(MIMEText(body))
    if html is not None:
        message.attach(MIMEText(html, "html"))
    smtp = SMTP(host=MAIL_SERVER, port=MAIL_PORT)
    smtp.login(user=MAIL_USERNAME, password=MAIL_PASSWORD)
    smtp.send_message(msg=message)
    smtp.quit()