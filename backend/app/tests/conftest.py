from pytest import fixture
from sanic import Sanic
from sanic_testing import TestManager
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker

from app import create_app
from app.core.database import Base, engine
from app.models.todos import Todo
from app.models.users import User
from app.tests.factories import UserFactory, TodoFactory


@fixture(scope="session")
def app() -> Sanic:
    """
    Initializes the app for testing.

    :return: The initialized app.
    """
    app = create_app()
    TestManager(app=app)
    return app


@fixture(scope="session")
def test_connection() -> Connection:
    """
    Creates a database connection for testing.

    :return: The created database connection.
    """
    connection = engine.connect()
    Base.metadata.bind = connection
    Base.metadata.create_all()
    yield connection
    Base.metadata.drop_all()


@fixture(scope="session")
def session_factory(test_connection: Connection) -> Session:
    return sessionmaker(bind=test_connection)


@fixture(autouse=True)
def session(session_factory: Session) -> Session:
    """
    Creates a session for testing.

    :return: The created session.
    """
    session = session_factory()
    try:
        yield session
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


@fixture
def user(session: Session) -> User:
    """
    Creates an user for testing.

    :return: The created user.
    """
    user = UserFactory()
    session.commit()
    return user


@fixture
def todo(user: User, session: Session) -> Todo:
    """
    Creates a todo for testing.

    :return: The created todo.
    """
    todo = TodoFactory(user=user)
    session.commit()
    return todo


@fixture
def foreign_todo(session: Session) -> Todo:
    """
    Creates a todo that belongs to another
    user for testing.

    :return: The created todo.
    """
    todo = TodoFactory()
    session.commit()
    return todo