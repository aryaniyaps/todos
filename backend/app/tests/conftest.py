import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.extensions import db
from app.models.users import User
from app.models.todos import Todo
from app.services.users import create_user
from app.services.todos import create_todo


@pytest.fixture(scope="session")
def app() -> Flask:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    app = create_app(config="app.tests.settings")
    context = app.test_request_context()
    context.push()
    yield app
    context.pop()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    :return: An HTTP test client.
    """
    yield app.test_client()


@pytest.fixture(scope="session")
def db(app: Flask) -> SQLAlchemy:
    """
    Sets up the database for tests.

    :return: the test database.
    """
    db.app = app
    with app.app_context():
        db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(autouse=True)
def session(db: SQLAlchemy):
    """
    Sets up transactions for every test case.

    :return: A session wrapped in a transaction.
    """
    db.session.begin_nested()
    yield db.session
    db.session.rollback()


@pytest.fixture
def test_user() -> User:
    """
    Creates an user instance for testing.
    """
    return create_user(
        email="user@example.org",
        password="password"
    )


@pytest.fixture
def test_todo(test_user: User) -> Todo:
    """
    Creates a todo instance for testing.
    """
    return create_todo(
        content="sample content",
        user_id=test_user.id
    )