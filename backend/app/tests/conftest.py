import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.models.users import User
from app.services.users import create_user


@pytest.fixture(scope="session")
def app() -> Flask:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    app = create_app()
    context = app.app_context()
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
    app.db.create_all()
    yield app.db
    app.db.drop_all()


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
    return create_user(
        email="test@gmail.com",
        password="password"
    )