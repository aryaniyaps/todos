"""
Configuration options for development/ production.
"""
from starlette.config import Config


config = Config()

# whether the app is in development.
DEBUG = config("DEBUG", cast=bool, default=False)

# branding configuration.
SITE_NAME = config("SITE_NAME", default="todos")

# sqlalchemy database URL.
DATABASE_URL = config("DATABASE_URL")

# mail server name.
MAIL_SERVER = config("MAIL_SERVER", default="localhost")

# mail client port.
MAIL_PORT = config("MAIL_PORT", cast=int, default=25)

# whether the mail client should use tls.
MAIL_USE_TLS = config("MAIL_USE_TLS", cast=bool, default=True)

# mail client auth username.
MAIL_USERNAME = config("MAIL_USERNAME", default=None)

# mail client auth password.
MAIL_PASSWORD = config("MAIL_PASSWORD", default=None)
