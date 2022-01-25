from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base, 
    scoped_session, 
    sessionmaker
)

from app.config import DEBUG, DATABASE_URL

Base = declarative_base()

engine = create_engine(url=DATABASE_URL, future=True, echo=DEBUG)

db_session = scoped_session(sessionmaker(bind=engine))


def shutdown_session(exception=None) -> None:
    """
    Shuts down the database session.
    """
    db_session.remove()
