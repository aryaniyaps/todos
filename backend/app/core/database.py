from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from app.core.config import DEBUG, DATABASE_URL

Base = declarative_base()

engine = create_engine(
    future=True,
    url=DATABASE_URL,
    echo=DEBUG,
)

session_factory = sessionmaker(bind=engine)

db_session = scoped_session(session_factory)
