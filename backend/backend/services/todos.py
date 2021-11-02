from typing import Optional

from sqlalchemy.orm import Session

from backend.models.todos import Todo


def create_todo(session: Session, content: str, user_id: int) -> Todo:
    """
    Creates a new todo.
    """
    todo = Todo(content=content, user_id=user_id)
    session.add(instance=todo)
    session.commit()
    session.refresh(instance=todo)
    return todo


def update_todo(
    session: Session, 
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
    session.commit()
    session.refresh(instance=todo)
    return todo


def delete_todo(session: Session, todo: Todo) -> None:
    """
    Deletes the given todo.
    """
    session.delete(instance=todo)
    session.commit()