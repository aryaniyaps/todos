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
    app = create_app("app.tests.settings")
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def viewer_client(app: Flask) -> FlaskClient:
    """
    Creates an anonymous test client.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client()


@pytest.fixture(scope="session")
def user_client(app: Flask) -> FlaskClient:
    """
    Creates an authenticated test client.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client()


@pytest.fixture(scope="session")
def test_db(app: Flask) -> SQLAlchemy:
    """
    Sets up the database for tests.

    :return: The test database.
    """
    app.db = db
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(autouse=True)
def session(test_db: SQLAlchemy):
    """
    Creates a session enclosed in a transaction.

    :return: The created session.
    """
    connection = test_db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    session = test_db.create_scoped_session(options=options)

    test_db.session = session
    yield session

    transaction.rollback()
    connection.close()
    session.remove()

@pytest.fixture
def user() -> User:
    """
    Creates an user for tests.

    :return: The created user.
    """
    return UserFactory()


@pytest.fixture
def todo(user: User) -> Todo:
    """
    Creates a todo for tests.

    :return: The created todo.
    """
    return TodoFactory(user=user)


@pytest.fixture
def foreign_user() -> User:
    """
    Creates a foreign user for tests.

    :return: The created user.
    """
    return UserFactory()


@pytest.fixture
def foreign_todo(foreign_user: User) -> Todo:
    """
    Creates a todo that belongs to a foreign
    user for tests.

    :return: The created todo.
    """
    return TodoFactory(user=foreign_user)