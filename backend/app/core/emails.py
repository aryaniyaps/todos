from typing import Optional

from flask_mail import Message

from app.extensions import mail


def send_mail(to: str, subject: str, body: str, html: Optional[str] = None) -> None:
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