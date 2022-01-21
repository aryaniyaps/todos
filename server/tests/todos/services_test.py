from app.database import db_session

from app.todos.entities import Todo
from app.todos.services import todo_service
from app.users.entities import User


def test_get_todos(user: User) -> None:
    """
    Ensure we can get todos for a given user.
    """
    results = todo_service.get_todos(user=user)
    assert results == user.todos


def test_get_todo(todo: Todo) -> None:
    """
    Ensure we can get a todo.
    """
    result = todo_service.get_todo(
        todo_id=todo.id, 
        user=todo.user,
    )
    assert result == todo


def test_create_todo(user: User) -> None:
    """
    Ensure we can create a todo.
    """
    content = "sample content"
    result = todo_service.create_todo(
        content=content,
        user=user,
    )
    assert result.content == content
    assert result.user_id == user.id
    assert not result.completed


def test_update_todo(todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    content = "sample content"
    result = todo_service.update_todo(
        user=todo.user,
        todo_id=todo.id, 
        completed=True, 
        content=content,
    )
    assert result.content == content
    assert result.completed


def test_delete_todo(todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    todo_service.delete_todo(user=todo.user, todo_id=todo.id)
    assert not db_session.get(Todo, todo.id)


def test_clear_todos(user: User) -> None:
    """
    Ensure we can clear todos for a user.
    """
    todo_service.clear_todos(user=user)
    assert not user.todos
