import pytest
from sanic import Sanic
from sqlalchemy.orm import Session

from app import create_app
from app.core.database import Base
from app.models.todos import Todo
from app.models.users import User
from app.tests.factories import UserFactory, TodoFactory


@pytest.fixture(scope="session")
def app() -> Sanic:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    return create_app()


@pytest.fixture(scope="session")
def test_db(app: Sanic) -> SQLAlchemy:
    """
    Sets up the database for tests.

    :return: The test database.
    """
    Base.metadata.create_all()
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()


@pytest.fixture(autouse=True)
def session(test_db: SQLAlchemy):
    """
    Creates a session enclosed in a transaction.

    :return: The created session.
    """
    test_db.session.begin_nested()
    yield test_db.session
    test_db.session.remove()


@pytest.fixture
def user(session: Session) -> User:
    """
    Creates an user for tests.

    :return: The created user.
    """
    user = UserFactory()
    session.commit()
    return user


@pytest.fixture
def todo(user: User, session: Session) -> Todo:
    """
    Creates a todo for tests.

    :return: The created todo.
    """
    todo = TodoFactory(user=user)
    session.commit()
    return todo


@pytest.fixture
def foreign_todo(session: Session) -> Todo:
    """
    Creates a todo that belongs to another
    user for tests.

    :return: The created todo.
    """
    todo = TodoFactory()
    session.commit()
    return todo