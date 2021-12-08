"""
Configuration options for development/ production.
"""

from typing import Optional
from os import getenv


# branding configuration.
PUBLIC_SITE_NAME: str = getenv("PUBLIC_SITE_NAME", default="Todos")

# session secret configuration.
SECRET_KEY: str = getenv("SECRET_KEY")

# sqlalchemy database URL.
DATABASE_URL: str = getenv("DATABASE_URL")

# whether modifications are tracked.
DATABASE_TRACK_MODIFICATIONS: bool = False

# mail server name.
MAIL_SERVER: str = getenv("MAIL_SERVER", default="localhost")

# mail client port.
MAIL_PORT: int = int(getenv("MAIL_PORT", default=25))

# whether the mail client should use tls.
MAIL_USE_TLS: bool = bool(getenv("MAIL_USE_TLS", default=True))

# mail client auth username.
MAIL_USERNAME: Optional[str] = getenv("MAIL_USERNAME", default=None)

# mail client auth password.
MAIL_PASSWORD: Optional[str] = getenv("MAIL_PASSWORD", default=None)

# mail client sender address.
MAIL_DEFAULT_SENDER: str = getenv("MAIL_DEFAULT_SENDER")

# whether mail sending is disabled.
MAIL_SUPPRESS_SEND: bool = bool(getenv("MAIL_SUPPRESS_SEND", default=False))
