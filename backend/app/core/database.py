from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

Base = declarative_base()

engine = create_engine(
    future=True,
    url=settings.DATABASE_URL,
    echo=settings.DEBUG,
)

session_factory = sessionmaker(bind=engine)
