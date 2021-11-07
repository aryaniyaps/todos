from flask.templating import render_template
from flask_mail import Message

from app.extensions import mail
from app.models.users import User


def send_user_created_mail(recipient: str, user: User) -> None:
    """
    Sends an mail to a newly created user.

    :param recipient: The address to send the mail to.
    :param user: The newly created user.
    """
    subject = f"New account created"
    html = render_template("emails/user_created.html", user=user)
    message = Message(subject=subject, html=html)
    message.add_recipient(recipient=recipient)
    mail.send(message=message)