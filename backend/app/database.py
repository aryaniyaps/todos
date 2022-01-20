from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from app.core.config import DEBUG, DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL, future=True, echo=DEBUG)

session_factory = sessionmaker(bind=engine)

db_session = scoped_session(session_factory)


def teardown_session(exception=None) -> None:
    """
    Tears down the database session.
    """
    db_session.remove()
