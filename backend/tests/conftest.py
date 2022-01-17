from typing import Generator

from flask import Flask
from flask.testing import FlaskClient
from flask_login import FlaskLoginClient
from pytest import fixture

from app import create_app
from app.core.database import Base, engine
from app.todos.entities import Todo
from app.users.entities import User
from tests.factories import TodoFactory, UserFactory


def pytest_configure(config) -> None:
    """
    Setup test suite.
    """
    Base.metadata.create_all(engine)


def pytest_unconfigure(config) -> None:
    """
    Teardown test suite.
    """
    Base.metadata.drop_all(engine)


@fixture(scope="session")
def app() -> Flask:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    app = create_app()
    app.test_client_class = FlaskLoginClient
    return app


@fixture()
def client(app: Flask) -> Generator[FlaskClient, None, None]:
    """
    Creates a client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client()

@fixture()
def auth_client(app: Flask, user: User) -> Generator[FlaskClient, None, None]:
    """
    Creates an authenticated client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client(user=user)


@fixture()
def user() -> User:
    """
    Creates an user for testing.

    :return: The created user.
    """
    return UserFactory()


@fixture()
def todo(user: User) -> Todo:
    """
    Creates a todo for testing.

    :return: The created todo.
    """
    return TodoFactory(user=user)


@fixture()
def foreign_todo() -> Todo:
    """
    Creates a todo that belongs to another
    user for testing.

    :return: The created todo.
    """
    return TodoFactory()
