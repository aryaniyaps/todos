from http import HTTPStatus

from sanic import Sanic

from app.models.users import User


def test_login(app: Sanic, user: User) -> None:
    """
    Ensure we can log the current user in.
    """
    data = {"email": user.email, "password": "password"}
    request, response = app.test_client.post(app.url_for("app.auth.login"), json=data)
    assert response.status == HTTPStatus.OK


def test_logout(app: Sanic) -> None:
    """
    Ensure we can log the current user out.
    """
    request, response = app.test_client.post(app.url_for("app.auth.logout"))
    assert response.status == HTTPStatus.NO_CONTENT


def test_logout_unauthorized(app: Sanic) -> None:
    """
    Ensure we cannot logout anonymously.
    """
    request, response = app.test_client.post(app.url_for("app.auth.logout"))
    assert response.status == HTTPStatus.UNAUTHORIZED