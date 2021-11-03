from typing import Optional
from os import getenv


# branding configuration.
PUBLIC_SITE_NAME = getenv("PUBLIC_SITE_NAME", default="Todos")

# app environment.
ENV: str = getenv("FLASK_ENV", default="development")

# whether debug features are enabled.
DEBUG: bool = bool(getenv("FLASK_DEBUG", default=True))

# sqlalchemy database URL.
SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")

# whether modifications are tracked.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# elasticsearch configuration.
ELASTICSEARCH_URL: str = getenv("ELASTICSEARCH_URL")

# mail client host name.
MAIL_SERVER: str = getenv("MAIL_SERVER")

# mail client port.
MAIL_PORT: int = int(getenv("MAIL_PORT"))

# whether the mail client should use tls.
MAIL_USE_TLS = bool(getenv("MAIL_USE_TLS", default=True))

# mail client auth username.
MAIL_USERNAME: Optional[str] = getenv("MAIL_USERNAME", default=None)

# mail client auth password.
MAIL_PASSWORD: Optional[str] = getenv("MAIL_PASSWORD", default=None)

# mail client sender address.
MAIL_DEFAULT_SENDER: Optional[str] = getenv("MAIL_DEFAULT_SENDER", default=None)
