"""
Configuration options for development/ production.
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    # whether the app is in development.
    DEBUG: str = False
    # Prometheus metrics port.
    METRICS_PORT: int
    # branding configuration.
    SITE_NAME: str = "Todos"
    # SQLAlchemy database URL.
    DATABASE_URL: str
    # Celery broker URL.
    CELERY_BROKER_URL: str
    # Celery result expiration duration.
    CELERY_RESULT_EXPIRES: int
    # Celery result backend.
    CELERY_RESULT_BACKEND: str

    class Config:
        case_sensitive = True


settings = Settings()
