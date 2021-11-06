from http import HTTPStatus

from faker import Faker
from flask import url_for
from flask.testing import FlaskClient

from app.models.todos import Todo


def test_read_todos(client: FlaskClient) -> None:
    """
    Ensure we can read the current user's todos.
    """
    response = client.get(url_for("app.todos.read_todos"))
    assert response.status_code == HTTPStatus.OK


def test_create_todo(client: FlaskClient, faker: Faker) -> None:
    """
    Ensure we can create a todo.
    """
    data = {"content": faker.text(250)}
    response = client.post(url_for("app.todos.create_todo"), json=data)
    assert response.status_code == HTTPStatus.CREATED


def test_read_todo(client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can read a todo.
    """
    response = client.get(url_for("app.todos.read_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.OK


def test_read_foreign_todo(client: FlaskClient) -> None:
    """
    Ensure we cannot read a todo we don't own.
    """
    pass


def test_update_todo(client: FlaskClient, todo: Todo, faker: Faker) -> None:
    """
    Ensure we can update a todo.
    """
    data = {"content": faker.text(250), "completed": True}
    response = client.patch(url_for("app.todos.update_todo", todo_id=todo.id), json=data)
    assert response.status_code == HTTPStatus.OK


def test_update_foreign_todo(client: FlaskClient, faker: Faker) -> None:
    """
    Ensure we cannot update a todo we don't own.
    """
    pass


def test_delete_todo(client: FlaskClient, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    response = client.delete(url_for("app.todos.delete_todo", todo_id=todo.id))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_foreign_todo(client: FlaskClient) -> None:
    """
    Ensure we cannot delete a todo we don't own.
    """
    pass