from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app import settings

Base = declarative_base()

engine = create_engine(
    future=True,
    url=settings.DATABASE_URL, 
    echo=settings.DEBUG, 
)


@contextmanager
def get_session(engine: Engine = engine) -> Generator[Session, None, None]:
    """
    Gets a session instance.

    :return: the obtained session.
    """
    session = sessionmaker(bind=engine)
    try:
        yield session
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()
