from pydantic import BaseSettings


class Settings(BaseSettings):
    # whether the app is in development.
    DEBUG: str = False
    # Prometheus metrics port.
    METRICS_PORT: int
    # SQLAlchemy database URL.
    DATABASE_URL: str
    # Celery broker URL.
    CELERY_BROKER_URL: str

    class Config:
        case_sensitive = True


settings = Settings()
