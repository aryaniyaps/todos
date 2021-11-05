from http import HTTPStatus

from faker import Faker
from flask import url_for
from flask.testing import FlaskClient


def test_read_current_user(client: FlaskClient) -> None:
    """
    Ensure we can read the current user.
    """
    response = client.get(url_for("app.users.read_current_user"))
    assert response.status_code == HTTPStatus.OK


def test_create_user(client: FlaskClient, faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    data = {
        "email": faker.ascii_free_email(), 
        "password": faker.password(length=12)
    }
    response = client.post(url_for("app.users.create_user"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_duplicate_user(client: FlaskClient, faker: Faker) -> None:
    """
    Ensure we cannot create an user with an existing email.
    """
    response = client.post(url_for("app.users.create_user"), json={})
