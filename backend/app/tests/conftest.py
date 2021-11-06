import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.extensions import db
from app.models.todos import Todo
from app.models.users import User
from app.tests.factories import UserFactory, TodoFactory


@pytest.fixture(scope="session")
def app() -> Flask:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    app = create_app(config="app.tests.settings")
    with app.app_context():
        yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    :return: An HTTP test client.
    """
    with app.test_request_context():
        yield app.test_client()


@pytest.fixture(scope="session")
def test_db(app: Flask) -> SQLAlchemy:
    """
    Sets up the database for tests.

    :return: the test database.
    """
    app.db = db
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(autouse=True)
def session(test_db: SQLAlchemy):
    """
    Sets up transactions for every test case.

    :return: A session wrapped in a transaction.
    """
    test_db.session.begin_nested()
    yield test_db.session
    test_db.session.rollback()


@pytest.fixture
def user() -> User:
    """
    Creates an user for tests.

    :return: The created user.
    """
    return UserFactory()


@pytest.fixture
def todo() -> Todo:
    """
    Creates a todo for tests.

    :return: The created todo.
    """
    return TodoFactory()