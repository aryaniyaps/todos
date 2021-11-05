import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.extensions import db as _db


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
    return app.test_client()


@pytest.fixture(scope="session")
def db(app: Flask) -> SQLAlchemy:
    """
    Sets up the database for tests.

    :return: the test database.
    """
    _db.create_all()
    yield _db
    _db.session.remove()
    _db.drop_all()


@pytest.fixture(autouse=True)
def session(db: SQLAlchemy):
    """
    Sets up transactions for every test case.

    :return: A session wrapped in a transaction.
    """
    db.session.begin_nested()
    yield db.session
    db.session.rollback()