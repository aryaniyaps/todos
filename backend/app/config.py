"""
Configuration options for development/ production.
"""
from starlette.config import Config


config = Config()

# whether the app is in development.
DEBUG = config("DEBUG", cast=bool, default=False)

# branding configuration.
SITE_NAME = config("SITE_NAME", cast=str, default="todos")

# SQLAlchemy database URL.
DATABASE_URL = config("DATABASE_URL", cast=str)

# mail server name.
MAIL_SERVER = config("MAIL_SERVER", cast=str, default="localhost")

# mail client port.
MAIL_PORT = config("MAIL_PORT", cast=int, default=25)

# whether the mail client should use tls.
MAIL_USE_TLS = config("MAIL_USE_TLS", cast=bool, default=True)

# mail client auth username.
MAIL_USERNAME = config("MAIL_USERNAME", cast=str)

# mail client auth password.
MAIL_PASSWORD = config("MAIL_PASSWORD", cast=str)

# Celery broker URL.
CELERY_BROKER_URL = config("CELERY_BROKER_URL", cast=str)

# Celery result expiration duration.
CELERY_RESULT_EXPIRES = config("CELERY_RESULT_EXPIRES", cast=int)

# Celery result backend.
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", cast=str)
