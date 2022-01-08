from typing import Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session, scoped_session
from sqlalchemy.orm.session import sessionmaker

from app import create_app
from app.core.database import Base, engine
from app.entities.todos import Todo
from app.entities.users import User
from app.tests.factories import TodoFactory, UserFactory


@fixture(scope="session")
def app() -> FastAPI:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    return create_app()


@fixture()
def client(app: FastAPI) -> TestClient:
    """
    Creates a client for testing.

    :return: The created test client.
    """
    with TestClient(app) as client:
        return client

@fixture()
def auth_client() -> TestClient:
    """
    Creates an authenticated client for testing.

    :return: The created test client.
    """
    with TestClient(app) as client:
        # TODO: add auth headers.
        return client


@fixture(scope="session")
def test_connection() -> Generator[Connection, None, None]:
    """
    Creates a database connection for testing.

    :return: The created database connection.
    """
    connection = engine.connect()
    Base.metadata.bind = connection
    Base.metadata.create_all()
    yield connection
    Base.metadata.drop_all()


@fixture(scope="session")
def session_factory(test_connection: Connection) -> Session:
    return scoped_session(sessionmaker(test_connection))


@fixture()
def session(session_factory: Session) -> Generator[Session, None, None]:
    """
    Creates a session for testing.

    :return: The created session.
    """
    session = session_factory()
    yield session
    session.rollback()
    session.close()


@fixture()
def user(session: Session) -> User:
    """
    Creates an user for testing.

    :return: The created user.
    """
    user = UserFactory()
    session.add(user)
    session.commit()
    return user


@fixture()
def todo(user: User, session: Session) -> Todo:
    """
    Creates a todo for testing.

    :return: The created todo.
    """
    todo = TodoFactory(user=user)
    session.add(todo)
    session.commit()
    return todo


@fixture()
def foreign_todo(session: Session) -> Todo:
    """
    Creates a todo that belongs to another
    user for testing.

    :return: The created todo.
    """
    todo = TodoFactory()
    session.add(todo)
    session.commit()
    return todo
