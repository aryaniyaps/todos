from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from app.models.users import User


def test_authenticate_user(client: FlaskClient, user: User) -> None:
    """
    Ensure we can log the current user in.
    """
    data = {"email": user.email, "password": ""}
    response = client.post(url_for("app.auth.authenticate_user"), json=data)
    assert response.status_code == HTTPStatus.OK


def test_unauthenticate_user(client: FlaskClient) -> None:
    """
    Ensure we can log the current user out.
    """
    response = client.post(url_for("app.auth.unauthenticate_user"))
    assert response.status_code == HTTPStatus.NO_CONTENT