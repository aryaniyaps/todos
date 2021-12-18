from http import HTTPStatus

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.models.users import User


def test_read_current_user(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we can read the current user.
    """
    response = client.get(app.url_path_for("users:current"))
    assert response.status_code == HTTPStatus.OK


def test_read_current_user_unauthorized(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we cannot read the current user anonymously.
    """
    response = client.get(app.url_path_for("users:current"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_user(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we can create an user.
    """
    data = {"email": "user@example.org", "password": "password"}
    response = client.post(app.url_path_for("users:create"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_create_duplicate_user(app: FastAPI, client: TestClient, user: User) -> None:
    """
    Ensure we cannot create an user with a duplicate email.
    """
    data = {"email": user.email, "password": "password"}
    response = client.post(app.url_path_for("users:create"), json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
