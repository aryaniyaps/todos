"""
Configuration options for development/ production.
"""
from os import getenv

# whether the app is in development.
DEBUG = bool(getenv("DEBUG", default=False))

# branding configuration.
PUBLIC_SITE_NAME = getenv("PUBLIC_SITE_NAME", default="Todos")

# sqlalchemy database URL.
DATABASE_URL = getenv("DATABASE_URL")

# mail server name.
MAIL_SERVER = getenv("MAIL_SERVER", default="localhost")

# mail client port.
MAIL_PORT = int(getenv("MAIL_PORT", default=25))

# whether the mail client should use tls.
MAIL_USE_TLS = bool(getenv("MAIL_USE_TLS", default=True))

# mail client auth username.
MAIL_USERNAME = getenv("MAIL_USERNAME", default=None)

# mail client auth password.
MAIL_PASSWORD = getenv("MAIL_PASSWORD", default=None)
