import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.services.users import create_user


@pytest.fixture(scope="session")
def app() -> Flask:
    app = create_app()
    context = app.test_request_context()
    context.push()
    yield app
    context.pop()


@pytest.fixture(scope="function")
def client(app: Flask) -> FlaskClient:
    yield app.test_client()


@pytest.fixture(scope="session")
def db(app: Flask) -> SQLAlchemy:
    app.db.create_all()
    yield app.db
    app.db.drop_all()


@pytest.fixture(scope="function")
def session(db: SQLAlchemy):
    db.session.begin_nested()
    yield db.session
    db.session.rollback()


@pytest.fixture(scope="function")
def test_user(session):
    return create_user(
        email="test@gmail.com",
        password="password"
    )