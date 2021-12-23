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

# Celery broker URL.
CELERY_BROKER_URL = config("CELERY_BROKER_URL", cast=str)

# Celery result expiration duration.
CELERY_RESULT_EXPIRES = config("CELERY_RESULT_EXPIRES", cast=int)

# Celery result backend.
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", cast=str)
