from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, pool_size=20, future=True)


@contextmanager
def get_session(engine: Engine = engine) -> Generator[Session, None]:
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
