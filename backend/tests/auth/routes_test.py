from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from app.users.entities import User


def test_login(client: FlaskClient, user: User) -> None:
    """
    Ensure we can log the current user in.
    """
    data = {"email": user.email, "password": "password"}
    response = client.post(url_for("auth.login"), json=data)
    assert response.status_code == HTTPStatus.OK


def test_logout(auth_client: FlaskClient) -> None:
    """
    Ensure we can log the current user out.
    """
    response = auth_client.post(url_for("auth.logout"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_logout_unauthorized(client: FlaskClient) -> None:
    """
    Ensure we cannot logout anonymously.
    """
    response = client.post(url_for("auth.logout"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED
