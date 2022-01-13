from sqlalchemy.orm import Session

from app.entities.todos import Todo
from app.entities.users import User
from app.services.todos import TodoService


def test_get_todos(session: Session, user: User) -> None:
    """
    Ensure we can get todos for a given user.
    """
    result = TodoService(session).get_todos(user_id=user.id)
    assert result == user.todos


def test_get_todo(session: Session, todo: Todo) -> None:
    """
    Ensure we can get a todo with a given ID and user ID.
    """
    result = TodoService(session).get_todo(
        todo_id=todo.id, 
        user_id=todo.user_id,
    )
    assert result == todo


def test_create_todo(session: Session, user: User) -> None:
    """
    Ensure we can create a todo.
    """
    content = "sample content"
    result = TodoService(session).create_todo(
        content=content,
        user_id=user.id,
    )
    assert result.content == content
    assert result.user_id == user.id
    assert not result.completed


def test_update_todo(session: Session, todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    content = "sample content"
    result = TodoService(session).update_todo(
        todo=todo, 
        completed=True, 
        content=content,
    )
    assert result.content == content
    assert result.completed


def test_delete_todo(session: Session, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    TodoService(session).delete_todo(todo=todo)
    assert not session.get(Todo, todo.id)


def test_clear_todos(session: Session, user: User) -> None:
    """
    Ensure we can clear todos for a user.
    """
    TodoService(session).clear_todos(user_id=user.id)
    assert not user.todos.first()
