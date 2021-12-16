from pytest import fixture
from sanic import Sanic
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app import create_app
from app.core.database import get_session
from app.models.todos import Todo
from app.models.users import User
from app.tests.factories import UserFactory, TodoFactory


@fixture(scope="session")
def app() -> Sanic:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    return create_app()


@fixture(scope="session")
def test_engine() -> Engine:
    """
    Creates a database engine for testing.

    :return: The created database engine.
    """
    return create_engine()


@fixture(autouse=True)
def session(test_engine: Engine):
    """
    Creates a session for testing.

    :return: The created session.
    """
    with get_session(test_engine) as session:
        yield session


@fixture
def user(session: Session) -> User:
    """
    Creates an user for tests.

    :return: The created user.
    """
    user = UserFactory()
    session.commit()
    return user


@fixture
def todo(user: User, session: Session) -> Todo:
    """
    Creates a todo for tests.

    :return: The created todo.
    """
    todo = TodoFactory(user=user)
    session.commit()
    return todo


@fixture
def foreign_todo(session: Session) -> Todo:
    """
    Creates a todo that belongs to another
    user for tests.

    :return: The created todo.
    """
    todo = TodoFactory()
    session.commit()
    return todo