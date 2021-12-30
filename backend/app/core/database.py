from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

Base = declarative_base()

engine = create_engine(
    future=True,
    url=settings.DATABASE_URL,
    echo=settings.DEBUG,
)

session_factory = sessionmaker(bind=engine)
