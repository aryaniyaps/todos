from app.extensions import mail
from app.core.emails import send_mail


def test_send_mail() -> None:
    """
    Ensure we can send emails.
    """
    subject = "test mail subject"
    recipient = "recipient@example.org"
    body = "test mail body"
    html = "<p>Hello world!</p>"
    with mail.record_messages() as outbox:
        send_mail(to=recipient, subject=subject, body=body, html=html)
        assert len(outbox) == 1
        sent_message = outbox[0]
        assert sent_message.subject == subject
        assert sent_message.recipients == [recipient]
        assert sent_message.body == body
        assert sent_message.html == html
        assert "Content-Type: text/html" in sent_message.as_string()