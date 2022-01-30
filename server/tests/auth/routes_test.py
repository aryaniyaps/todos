from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from app.users.entities import User


def test_authenticate(client: FlaskClient, user: User) -> None:
    """
    Ensure we can authenticate the current user.
    """
    data = {"email": user.email, "password": "password"}
    response = client.post(url_for("auth.authenticate"), json=data)
    assert response.status_code == HTTPStatus.OK


def test_authenticate_invalid(client: FlaskClient, user: User) -> None:
    """
    Ensure we cannot authenticate the current user
    with invalid credentials.
    """
    data = {"email": user.email, "password": "invalid-password"}
    response = client.post(url_for("auth.authenticate"), json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_unauthenticate(auth_client: FlaskClient) -> None:
    """
    Ensure we can unauthenticate the current user.
    """
    response = auth_client.post(url_for("auth.unauthenticate"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_unauthenticate_unauthorized(client: FlaskClient) -> None:
    """
    Ensure we cannot unauthenticate anonymously.
    """
    response = client.post(url_for("auth.unauthenticate"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED
