from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL, DEBUG

Base = declarative_base()

engine = create_engine(
    future=True,
    url=DATABASE_URL,
    echo=DEBUG,
)

session_factory = sessionmaker(bind=engine)
