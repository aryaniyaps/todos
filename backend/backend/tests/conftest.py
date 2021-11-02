import pytest

from backend import create_app
from backend.extensions import db


@pytest.fixture(scope="function")
def app():
    app = create_app()
    with app.app_context():
        db.create_all()

    context = app.test_request_context()
    context.push()
    yield app
    context.pop()


@pytest.fixture(scope="function")
def db(app):
    db.app = app
    with app.app_context():
        db.create_all()
    yield db
    db.session.close()
    db.drop_all()