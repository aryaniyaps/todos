from typing import Optional

from backend.extensions import db
from backend.models.todos import Todo


def create_todo(content: str, user_id: int) -> Todo:
    """
    Creates a new todo.
    """
    todo = Todo(content=content, user_id=user_id)
    db.session.add(instance=todo)
    db.session.commit()
    db.session.refresh(instance=todo)
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
    db.session.refresh(instance=todo)
    return todo


def delete_todo(todo: Todo) -> None:
    """
    Deletes the given todo.
    """
    db.session.delete(instance=todo)
    db.session.commit()