from http import HTTPStatus

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.models.todos import Todo


def test_read_todos(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we can read the current user's todos.
    """
    response = client.get(app.url_path_for("todos:read-all"))
    assert response.status_code == HTTPStatus.OK


def test_read_todos_unauthorized(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we cannot read todos anonymously.
    """
    response = client.get(app.url_path_for("todos:read-all"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_clear_todos(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we can clear the current user's todos.
    """
    response = client.delete(app.url_path_for("todos:clear"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_clear_todos_unauthorized(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we cannot clear todos anonymously.
    """
    response = client.delete(app.url_path_for("todos:clear"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_todo(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we can create a todo.
    """
    data = {"content": "sample content"}
    response = client.post(app.url_path_for("todos:create"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_create_todos_unauthorized(app: FastAPI, client: TestClient) -> None:
    """
    Ensure we cannot create a todo anonymously.
    """
    data = {"content": "sample content"}
    response = client.post(app.url_path_for("todos:create"), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_read_todo(app: FastAPI, client: TestClient, todo: Todo) -> None:
    """
    Ensure we can read a todo.
    """
    response = client.get(app.url_path_for("todos:read", todo_id=todo.id))
    assert response.status_code == HTTPStatus.OK


def test_read_todo_unauthorized(app: FastAPI, client: TestClient, todo: Todo) -> None:
    """
    Ensure we cannot read a todo anonymously.
    """
    response = client.get(app.url_path_for("todos:read", todo_id=todo.id))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_read_foreign_todo(app: FastAPI, client: TestClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot read a todo we don't own.
    """
    response = client.get(app.url_path_for("todos:read", todo_id=foreign_todo.id))
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_todo(app: FastAPI, client: TestClient, todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    data = {"content": "sample content", "completed": True}
    response = client.patch(app.url_path_for("todos:update", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.OK


def test_update_todo_unauthorized(app: FastAPI, client: TestClient, todo: Todo) -> None:
    """
    Ensure we cannot update a todo anonymously.
    """
    data = {"content": "sample content", "completed": True}
    response = client.patch(app.url_path_for("todos:update", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_update_foreign_todo(app: FastAPI, client: TestClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot update a todo we don't own.
    """
    data = {"content": "sample content", "completed": True}
    response = client.patch(app.url_path_for("todos:update", todo_id=foreign_todo.id), json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_todo(app: FastAPI, client: TestClient, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    response = client.delete(app.url_path_for("todos:delete", todo_id=todo.id))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_todo_unauthorized(app: FastAPI, client: TestClient, todo: Todo) -> None:
    """
    Ensure we cannot delete a todo anonymously.
    """
    response = client.delete(app.url_path_for("todos:delete", todo_id=todo.id))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_delete_foreign_todo(app: FastAPI, client: TestClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot delete a todo we don't own.
    """
    response = client.delete(app.url_path_for("todos:delete", todo_id=foreign_todo.id))
    assert response.status_code == HTTPStatus.NOT_FOUND
