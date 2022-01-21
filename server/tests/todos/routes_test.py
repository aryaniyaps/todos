from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from app.todos.entities import Todo


def test_read_todos(auth_client: FlaskClient) -> None:
    """
    Ensure we can read the current user's todos.
    """
    response = auth_client.get(url_for("todos.read_todos"))
    assert response.status_code == HTTPStatus.OK


def test_read_todos_unauthorized(client: FlaskClient) -> None:
    """
    Ensure we cannot read todos anonymously.
    """
    response = client.get(url_for("todos.read_todos"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_clear_todos(auth_client: FlaskClient) -> None:
    """
    Ensure we can clear the current user's todos.
    """
    response = auth_client.delete(url_for("todos.clear_todos"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_clear_todos_unauthorized(client: FlaskClient) -> None:
    """
    Ensure we cannot clear todos anonymously.
    """
    response = client.delete(url_for("todos.clear_todos"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_todo(auth_client: FlaskClient) -> None:
    """
    Ensure we can create a todo.
    """
    data = {"content": "sample content"}
    response = auth_client.post(url_for("todos.create_todo"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_create_todo_unauthorized(client: FlaskClient) -> None:
    """
    Ensure we cannot create a todo anonymously.
    """
    data = {"content": "sample content"}
    response = client.post(url_for("todos.create_todo"), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_read_todo(auth_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can read a todo.
    """
    response = auth_client.get(url_for("todos.read_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.OK


def test_read_todo_unauthorized(client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we cannot read a todo anonymously.
    """
    response = client.get(url_for("todos.read_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_read_foreign_todo(auth_client: FlaskClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot read a todo we don't own.
    """
    response = auth_client.get(url_for("todos.read_todo", todo_id=foreign_todo.id))
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_todo(auth_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    data = {"content": "sample content", "completed": True}
    response = auth_client.patch(url_for("todos.update_todo", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.OK


def test_update_todo_unauthorized(client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we cannot update a todo anonymously.
    """
    data = {"content": "sample content", "completed": True}
    response = client.patch(url_for("todos.update_todo", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_update_foreign_todo(auth_client: FlaskClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot update a todo we don't own.
    """
    data = {"content": "sample content", "completed": True}
    response = auth_client.patch(url_for("todos.update_todo", todo_id=foreign_todo.id), json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_todo(auth_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    response = auth_client.delete(url_for("todos.delete_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_todo_unauthorized(client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we cannot delete a todo anonymously.
    """
    response = client.delete(url_for("todos.delete_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_delete_foreign_todo(auth_client: FlaskClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot delete a todo we don't own.
    """
    response = auth_client.delete(url_for("todos.delete_todo", todo_id=foreign_todo.id))
    assert response.status_code == HTTPStatus.NOT_FOUND
