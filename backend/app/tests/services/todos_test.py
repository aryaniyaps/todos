from sqlalchemy.orm import Session

from app.models.users import User
from app.models.todos import Todo


def test_get_todos(session: Session, user: User) -> None:
    """
    Ensure we can get todos for a given user.
    """
    pass


def test_get_todo(session: Session, todo: Todo) -> None:
    """
    Ensure we can get a todo with a given ID and user ID.
    """
    pass


def test_create_todo(session: Session, user: User) -> None:
    """
    Ensure we can create a todo.
    """
    pass


def test_update_todo(session: Session, todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    pass


def test_delete_todo(session: Session, todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    pass


def test_clear_todos(session: Session, user: User) -> None:
    """
    Ensure we can clear todos for a user.
    """
    pass