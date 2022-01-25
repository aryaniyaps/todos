from typing import Iterator

from alembic.command import stamp
from alembic.config import Config
from flask import Flask
from flask.testing import FlaskClient
from flask_login import FlaskLoginClient
from pytest import fixture
from sqlalchemy.engine import Connection, Engine
from sqlalchemy.orm import Session

from app import create_app
from app.database import Base, db_session, engine
from app.todos.entities import Todo
from app.todos.services import todo_service
from app.users.entities import User
from app.users.services import user_service


@fixture(scope="session")
def app() -> Flask:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    app = create_app()
    app.test_client_class = FlaskLoginClient
    return app


@fixture(scope="session")
def db_engine() -> Iterator[Engine]:
    alembic_cfg = Config("alembic.ini")
    Base.metadata.create_all(bind=engine)
    stamp(alembic_cfg, revision="head")
    yield engine
    Base.metadata.drop_all(bind=engine)
    stamp(alembic_cfg, revision=None, purge=True)


@fixture(scope="session")
def db_connection(db_engine: Engine) -> Iterator[Connection]:
    """
    Initializes the connection to 
    the test database.

    :return: The database connection.
    """
    connection = db_engine.connect()
    yield connection
    connection.close()


@fixture(autouse=True)
def db_transaction(db_connection: Connection) -> Iterator[Session]:
    """
    Sets up a database transaction for each test case.

    :return: The database transaction.
    """
    transaction = db_connection.begin()
    session = db_session(bind=db_connection)
    yield session
    session.close()
    transaction.rollback()


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
def foreign_todo() -> Todo:
    """
    Creates a foreign todo for testing.

    :return: The created todo.
    """
    return todo_service.create_todo(
        content="sample content",
        user=user_service.create_user(
            email="foreign-tester@example.org",
            password="password",
        )
    )
