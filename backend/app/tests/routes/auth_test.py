from http import HTTPStatus

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.models.users import User


def test_login(app: FastAPI, client: TestClient, user: User) -> None:
    """
    Ensure we can log the current user in.
    """
    data = {"email": user.email, "password": "password"}
    response = client.post(app.url_path_for("auth:login"), json=data)
    assert response.status_code == HTTPStatus.OK


def test_logout(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we can log the current user out.
    """
    response = client.post(app.url_path_for("auth:logout"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_logout_unauthorized(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we cannot logout anonymously.
    """
    response = client.post(app.url_path_for("auth:logout"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED
