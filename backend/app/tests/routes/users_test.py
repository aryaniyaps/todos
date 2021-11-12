from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from app.models.users import User


def test_read_current_user(user_client: FlaskClient) -> None:
    """
    Ensure we can read the current user.
    """
    response = user_client.get(url_for("app.users.read_current_user"))
    assert response.status_code == HTTPStatus.OK


def test_read_current_user_unauthorized(viewer_client: FlaskClient) -> None:
    """
    Ensure we cannot read the current user anonymously.
    """
    response = viewer_client.get(url_for("app.users.read_current_user"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_user(viewer_client: FlaskClient) -> None:
    """
    Ensure we can create an user.
    """
    data = {"email": "user@example.org", "password": "password"}
    response = viewer_client.post(url_for("app.users.create_user"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_create_duplicate_user(viewer_client: FlaskClient, user: User) -> None:
    """
    Ensure we cannot create an user with a duplicate email.
    """
    data = {"email": user.email, "password": "password"}
    response = viewer_client.post(url_for("app.users.create_user"), json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
