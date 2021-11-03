from app.extensions import mail
from flask_mail import Message


def send_mail(to: str, subject: str, html: str, body: str) -> None:
    """
    Sends an individual mail to the
    specified recipient, with the given
    subject and template.
    """
    message = Message(
        subject=subject,
        body=body,
        html=html
    )
    message.add_recipient(to)
    mail.send(message)