from http import HTTPStatus

from fastapi.testclient import TestClient

from app.models.users import User


def test_read_current_user(client: TestClient) -> None:
    """
    Ensure we can read the current user.
    """
    response = client.get(app.url_for("app.users.read_current_user"))
    assert response.status_code == HTTPStatus.OK


def test_read_current_user_unauthorized(client: TestClient) -> None:
    """
    Ensure we cannot read the current user anonymously.
    """
    response = client.get(app.url_for("app.users.read_current_user"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_user(client: TestClient) -> None:
    """
    Ensure we can create an user.
    """
    data = {"email": "user@example.org", "password": "password"}
    response = client.post(app.url_for("app.users.create_user"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_create_duplicate_user(client: TestClient, user: User) -> None:
    """
    Ensure we cannot create an user with a duplicate email.
    """
    data = {"email": user.email, "password": "password"}
    response = client.post(app.url_for("app.users.create_user"), json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
