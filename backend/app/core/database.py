from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, future=True)

session_factory = sessionmaker(bind=engine)


@contextmanager
def get_session() -> Generator[Session, None]:
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
