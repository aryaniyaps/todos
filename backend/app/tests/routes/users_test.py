from http import HTTPStatus

from sanic import Sanic

from app.models.users import User


def test_read_current_user(app: Sanic) -> None:
    """
    Ensure we can read the current user.
    """
    request, response = app.test_client.get(app.url_for("app.users.read_current_user"))
    assert response.status == HTTPStatus.OK


def test_read_current_user_unauthorized(app: Sanic) -> None:
    """
    Ensure we cannot read the current user anonymously.
    """
    request, response = app.test_client.get(app.url_for("app.users.read_current_user"))
    assert response.status == HTTPStatus.UNAUTHORIZED


def test_create_user(app: Sanic) -> None:
    """
    Ensure we can create an user.
    """
    data = {"email": "user@example.org", "password": "password"}
    request, response = app.test_client.post(app.url_for("app.users.create_user"), json=data)
    assert response.status == HTTPStatus.CREATED


def test_create_duplicate_user(app: Sanic, user: User) -> None:
    """
    Ensure we cannot create an user with a duplicate email.
    """
    data = {"email": user.email, "password": "password"}
    request, response = app.test_client.post(app.url_for("app.users.create_user"), json=data)
    assert response.status == HTTPStatus.BAD_REQUEST
