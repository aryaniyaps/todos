from typing import Iterator

from alembic.command import stamp
from alembic.config import Config
from flask import Flask
from flask.testing import FlaskClient
from flask_login import FlaskLoginClient
from pytest import fixture
from sqlalchemy.engine import Connection, Engine

from app import create_app
from app.database.core import Base, db_session, engine
from app.todos.entities import Todo
from app.todos.repositories import todo_repo
from app.users.entities import User
from app.users.repositories import user_repo


@fixture(scope="session")
def app() -> Flask:
    """
    Initialize the app for testing.

    :return: The initialized app.
    """
    app = create_app()
    app.test_client_class = FlaskLoginClient
    return app


@fixture(scope="session")
def db_engine() -> Iterator[Engine]:
    """
    Set up the database engine.

    :return: The test database engine.
    """
    alembic_cfg = Config("alembic.ini")
    # create database tables.
    Base.metadata.create_all(bind=engine)
    # stamp the revisions table.
    stamp(alembic_cfg, revision="head")
    # yield database engine.
    yield engine
    # drop database tables.
    Base.metadata.drop_all(bind=engine)
    # stamp the revisions table.
    stamp(alembic_cfg, revision=None, purge=True)


@fixture(autouse=True)
def setup_transaction(db_engine: Engine) -> Iterator[Connection]:
    """
    Set up a transaction inside a database 
    connection for each test case.

    :return: The connection with transaction.
    """
    with db_engine.connect() as connection:
        # begin database transaction.
        transaction = connection.begin()
        # configure session bind.
        db_session.configure(bind=connection)
        # yield connection with transaction.
        yield connection
        # remove session instance.
        db_session.remove()
        # rollback database transaction.
        transaction.rollback()


@fixture()
def client(app: Flask) -> Iterator[FlaskClient]:
    """
    Create a client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client()
        

@fixture()
def auth_client(app: Flask, user: User) -> Iterator[FlaskClient]:
    """
    Create an authenticated client for testing.

    :return: The created test client.
    """
    with app.test_request_context():
        yield app.test_client(user=user)


@fixture()
def user() -> User:
    """
    Create an user for testing.

    :return: The created user.
    """
    return user_repo.create_user(
        email="tester@example.org",
        password="password"
    )


@fixture()
def foreign_user() -> User:
    """
    Create another user for checking
    authorization while testing.

    :return: The created user.
    """
    return user_repo.create_user(
        email="foreign-tester@example.org",
        password="password"
    )


@fixture()
def todo(user: User) -> Todo:
    """
    Create a todo for testing.

    :return: The created todo.
    """
    return todo_repo.create_todo(
        content="sample content",
        user_id=user.id
    )


@fixture()
def foreign_todo(foreign_user: User) -> Todo:
    """
    Create a todo that belongs to 
    another user for testing.

    :return: The created todo.
    """
    return todo_repo.create_todo(
        content="sample content",
        user_id=foreign_user.id
    )
