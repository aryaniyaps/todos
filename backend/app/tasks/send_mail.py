from typing import Optional

from app.worker import worker


@worker.task(name="send_email", bind=True)
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
    pass