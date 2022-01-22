from typing import Iterator

from flask import Flask
from flask.testing import FlaskClient
from flask_login import FlaskLoginClient
from pytest import fixture

from app import create_app
from app.database import Base, engine
from app.todos.entities import Todo
from app.todos.services import todo_service
from app.users.entities import User
from app.users.services import user_service


def pytest_sessionstart() -> None:
    """
    Setup test suite.
    """
    Base.metadata.create_all(engine)


def pytest_sessionfinish() -> None:
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
def test_connection():
    # TODO: return test connection here.
    pass


@fixture(autouse=True)
def setup_session(test_connection):
    # TODO: wrap session within transaction
    # refer: https://aalvarez.me/posts/python-transactional-tests-using-sqlalchemy-pytest-and-factory-boy/
    pass


@fixture()
def client(app: Flask) -> Iterator[FlaskClient]:
    """
    Creates a client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client()

@fixture()
def auth_client(app: Flask, user: User) -> Iterator[FlaskClient]:
    """
    Creates an authenticated client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client(user=user)


@fixture(scope="session")
def user() -> User:
    """
    Creates an user for testing.

    :return: The created user.
    """
    return user_service.create_user(
        email="tester@example.org",
        password="password"
    )


@fixture(scope="session")
def foreign_user() -> User:
    """
    Creates a foreign user for testing.

    :return: The created user.
    """
    return user_service.create_user(
        email="foreign-tester@example.org",
        password="password"
    )


@fixture(scope="session")
def todo(user: User) -> Todo:
    """
    Creates a todo for testing.

    :return: The created todo.
    """
    return todo_service.create_todo(
        content="sample content",
        user=user
    )


@fixture(scope="session")
def foreign_todo(foreign_user: User) -> Todo:
    """
    Creates a foreign todo for testing.

    :return: The created todo.
    """
    return todo_service.create_todo(
        content="sample content",
        user=foreign_user
    )