from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient

from app.models.todos import Todo


def test_read_todos(user_client: FlaskClient) -> None:
    """
    Ensure we can read the current user's todos.
    """
    response = user_client.get(url_for("app.todos.read_todos"))
    assert response.status_code == HTTPStatus.OK


def test_read_todos_unauthorized(viewer_client: FlaskClient) -> None:
    """
    Ensure we cannot read todos anonymously.
    """
    response = viewer_client.get(url_for("app.todos.read_todos"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_clear_todos(user_client: FlaskClient) -> None:
    """
    Ensure we can clear the current user's todos.
    """
    response = user_client.delete(url_for("app.todos.clear_todos"))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_clear_todos_unauthorized(viewer_client: FlaskClient) -> None:
    """
    Ensure we cannot clear todos anonymously.
    """
    response = viewer_client.delete(url_for("app.todos.clear_todos"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_create_todo(user_client: FlaskClient) -> None:
    """
    Ensure we can create a todo.
    """
    data = {"content": "sample content"}
    response = user_client.post(url_for("app.todos.create_todo"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_create_todos_unauthorized(viewer_client: FlaskClient) -> None:
    """
    Ensure we cannot create a todo anonymously.
    """
    data = {"content": "sample content"}
    response = viewer_client.post(url_for("app.todos.create_todo"), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_read_todo(user_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can read a todo.
    """
    response = user_client.get(url_for("app.todos.read_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.OK


def test_read_todo_unauthorized(viewer_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we cannot read a todo anonymously.
    """
    response = viewer_client.get(url_for("app.todos.read_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_read_foreign_todo(user_client: FlaskClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot read a todo we don't own.
    """
    response = user_client.get(url_for("app.todos.read_todo", todo_id=foreign_todo.id))
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_todo(user_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    data = {"content": "sample content", "completed": True}
    response = user_client.patch(url_for("app.todos.update_todo", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.OK


def test_update_todo_unauthorized(viewer_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we cannot update a todo anonymously.
    """
    data = {"content": "sample content", "completed": True}
    response = viewer_client.patch(url_for("app.todos.update_todo", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_update_foreign_todo(user_client: FlaskClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot update a todo we don't own.
    """
    data = {"content": "sample content", "completed": True}
    response = user_client.patch(url_for("app.todos.update_todo", todo_id=foreign_todo.id), json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_todo(user_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    response = user_client.delete(url_for("app.todos.delete_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_todo_unauthorized(viewer_client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we cannot delete a todo anonymously.
    """
    response = viewer_client.delete(url_for("app.todos.delete_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_delete_foreign_todo(user_client: FlaskClient, foreign_todo: Todo) -> None:
    """
    Ensure we cannot delete a todo we don't own.
    """
    response = user_client.delete(url_for("app.todos.delete_todo", todo_id=foreign_todo.id))
    assert response.status_code == HTTPStatus.NOT_FOUND