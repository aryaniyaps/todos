from typing import Generator

from flask import Flask
from flask.testing import FlaskClient
from pytest import fixture
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session, sessionmaker

from app import create_app
from app.core.database import Base, engine
from app.todos.entities import Todo
from app.users.entities import User
from tests.factories import TodoFactory, UserFactory


@fixture(scope="session")
def app() -> Flask:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    return create_app()


@fixture()
def client(app: Flask) -> FlaskClient:
    """
    Creates a client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        return app.test_client()

@fixture()
def auth_client(app: Flask) -> FlaskClient:
    """
    Creates an authenticated client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        # TODO: add auth cookies.
        return app.test_client()


@fixture(scope="session")
def test_connection() -> Generator[Connection, None, None]:
    """
    Creates a database connection for testing.

    :return: The created database connection.
    """
    with engine.begin() as connection:
        Base.metadata.create_all(connection)
        yield connection
        Base.metadata.drop_all(connection)


@fixture(scope="session")
def session_factory(test_connection: Connection) -> Session:
    return sessionmaker(test_connection)


@fixture()
def session(session_factory: Session) -> Session:
    """
    Creates a session for testing.

    :return: The created session.
    """
    with session_factory.begin() as session:
        return session


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
