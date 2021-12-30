from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from app.config import DATABASE_URL, DEBUG

Base = declarative_base()

engine = create_engine(
    future=True,
    url=DATABASE_URL,
    echo=DEBUG,
)

session_factory = sessionmaker(bind=engine)


def get_session() -> Generator[Session, None, None]:
    """
    Gets a session instance.

    :return: the obtained session.
    """
    session = session_factory()
    try:
        yield session
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()
