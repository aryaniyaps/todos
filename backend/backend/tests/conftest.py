import pytest

from backend import create_app
from backend.extensions import db


@pytest.fixture(scope="function")
def app():
    app = create_app()
    context = app.test_request_context()
    context.push()
    yield app
    context.pop()


@pytest.fixture(scope="session")
def db(app):
    with app.app_context():
        db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope="function")
def session(db):
    yield db.session
    db.session.close()
    db.session.rollback()