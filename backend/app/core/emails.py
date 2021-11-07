from app.extensions import mail
from flask_mail import Message


def send_mail(to: str, subject: str, html: str, body: str) -> None:
    """
    Sends an individual email.

    :param to: The recipient of the email.
    :param subject: The subject of the email.
    :param html: The HTML content of the email.
    :param body: The content of the email.
    """
    message = Message(
        subject=subject,
        body=body,
        html=html
    )
    message.add_recipient(to)
    mail.send(message)