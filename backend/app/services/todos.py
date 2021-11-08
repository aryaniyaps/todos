from typing import Optional

from app.extensions import db
from app.models.todos import Todo
from app.models.users import User


def create_todo(content: str, user_id: int) -> Todo:
    """
    Creates a new todo.
    """
    todo = Todo(content=content, user_id=user_id)
    db.session.add(todo)
    db.session.commit()
    db.session.refresh(todo)
    return todo


def update_todo(
    todo: Todo, 
    content: Optional[str], 
    completed: Optional[bool],
) -> Todo:
    """
    Updates the given todo.
    """
    if content is not None:
        todo.content = content
    if completed is not None:
        todo.completed = completed
    db.session.commit()
    db.session.refresh(todo)
    return todo


def delete_todo(todo: Todo) -> None:
    """
    Deletes the given todo.
    """
    db.session.delete(todo)
    db.session.commit()


def clear_todos(user: User) -> None:
    """
    Clears todos for the given user.
    """
    Todo.query.filter_by(user_id=user.id).delete()