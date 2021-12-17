from http import HTTPStatus

from sanic import Sanic

from app.models.todos import Todo


def test_read_todos(app: Sanic) -> None:
    """
    Ensure we can read the current user's todos.
    """
    request, response = app.test_client.get(app.url_for("app.todos.read_todos"))
    assert response.status == HTTPStatus.OK


def test_read_todos_unauthorized(app: Sanic) -> None:
    """
    Ensure we cannot read todos anonymously.
    """
    request, response = app.test_client.get(app.url_for("app.todos.read_todos"))
    assert response.status == HTTPStatus.UNAUTHORIZED


def test_clear_todos(app: Sanic) -> None:
    """
    Ensure we can clear the current user's todos.
    """
    request, response = app.test_client.delete(app.url_for("app.todos.clear_todos"))
    assert response.status == HTTPStatus.NO_CONTENT


def test_clear_todos_unauthorized(app: Sanic) -> None:
    """
    Ensure we cannot clear todos anonymously.
    """
    request, response = app.test_client.delete(app.url_for("app.todos.clear_todos"))
    assert response.status == HTTPStatus.UNAUTHORIZED


def test_create_todo(app: Sanic) -> None:
    """
    Ensure we can create a todo.
    """
    data = {"content": "sample content"}
    request, response = app.test_client.post(app.url_for("app.todos.create_todo"), json=data)
    assert response.status == HTTPStatus.CREATED


def test_create_todos_unauthorized(app: Sanic) -> None:
    """
    Ensure we cannot create a todo anonymously.
    """
    data = {"content": "sample content"}
    request, response = app.test_client.post(app.url_for("app.todos.create_todo"), json=data)
    assert response.status == HTTPStatus.UNAUTHORIZED


def test_read_todo(app: Sanic, todo: Todo) -> None:
    """
    Ensure we can read a todo.
    """
    request, response = app.test_client.get(app.url_for("app.todos.read_todo", todo_id=todo.id))
    assert response.status == HTTPStatus.OK


def test_read_todo_unauthorized(app: Sanic, todo: Todo) -> None:
    """
    Ensure we cannot read a todo anonymously.
    """
    request, response = app.test_client.get(app.url_for("app.todos.read_todo", todo_id=todo.id))
    assert response.status == HTTPStatus.UNAUTHORIZED


def test_read_foreign_todo(app: Sanic, foreign_todo: Todo) -> None:
    """
    Ensure we cannot read a todo we don't own.
    """
    request, response = app.test_client.get(app.url_for("app.todos.read_todo", todo_id=foreign_todo.id))
    assert response.status == HTTPStatus.NOT_FOUND


def test_update_todo(app: Sanic, todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    data = {"content": "sample content", "completed": True}
    request, response = app.test_client.patch(app.url_for("app.todos.update_todo", todo_id=todo.id), json=data)
    assert response.status == HTTPStatus.OK


def test_update_todo_unauthorized(app: Sanic, todo: Todo) -> None:
    """
    Ensure we cannot update a todo anonymously.
    """
    data = {"content": "sample content", "completed": True}
    request, response = app.test_client.patch(app.url_for("app.todos.update_todo", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_update_foreign_todo(app: Sanic, foreign_todo: Todo) -> None:
    """
    Ensure we cannot update a todo we don't own.
    """
    data = {"content": "sample content", "completed": True}
    request, response = app.test_client.patch(app.url_for("app.todos.update_todo", todo_id=foreign_todo.id), json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_todo(app: Sanic, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    request, response = app.test_client.delete(app.url_for("app.todos.delete_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_todo_unauthorized(app: Sanic, todo: Todo) -> None:
    """
    Ensure we cannot delete a todo anonymously.
    """
    request, response = app.test_client.delete(app.url_for("app.todos.delete_todo", todo_id=todo.id))
    assert response.status == HTTPStatus.UNAUTHORIZED


def test_delete_foreign_todo(app: Sanic, foreign_todo: Todo) -> None:
    """
    Ensure we cannot delete a todo we don't own.
    """
    request, response = app.test_client.delete(app.url_for("app.todos.delete_todo", todo_id=foreign_todo.id))
    assert response.status == HTTPStatus.NOT_FOUND