from http import HTTPStatus

from fastapi.testclient import TestClient

from app.models.users import User


def test_login(client: TestClient, user: User) -> None:
    """
    Ensure we can log the current user in.
    """
    data = {"email": user.email, "password": "password"}
    response = client.post(app.url_for("app.auth.login"), json=data)
    assert response.status_code == HTTPStatus.OK


def test_logout(client: TestClient) -> None:
    """
    Ensure we can log the current user out.
    """
    response = client.post(app.url_for("app.auth.logout"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_logout_unauthorized(client: TestClient) -> None:
    """
    Ensure we cannot logout anonymously.
    """
    response = client.post(app.url_for("app.auth.logout"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED