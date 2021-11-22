from typing import Optional

from flask_mail import Message

from app.core.celery import celery
from app.extensions import mail


@celery.task(bind=True)
def send_mail(
    recipient: str, 
    subject: str, 
    body: str, 
    html: Optional[str] = None
) -> None:
    """
    Sends an email to the given recipient.

    :param recipient: The recipient of the email.
    :param subject: The subject of the email.
    :param body: The body of the email.
    :param html: The HTML content of the email.
    """
    message = Message(subject=subject, body=body, html=html)
    message.add_recipient(recipient=recipient)
    mail.send(message=message)