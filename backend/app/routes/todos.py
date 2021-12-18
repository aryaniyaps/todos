from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.todos import Todo
from app.schemas.todos import TodoCreate, TodoUpdate


todo_router = APIRouter(prefix="/todos")


@todo_router.get("")
def read_todos(current_user, session: Session = Depends(get_session), offset: int = 1, limit: int = 20):
    """
    Get the current user's todos.
    """
    todos = session.query(Todo).filter_by(user_id=current_user.id)
    todos.offset(offset).limit(limit)
    return todos


@todo_router.post("", status_code=HTTPStatus.CREATED)
def create_todo(current_user, data: TodoCreate, session: Session = Depends(get_session)):
    """
    Create a new todo.
    """
    todo = Todo(
        content=data.content, 
        completed=data.completed,
        user_id=current_user.id
    )
    session.add(todo)
    session.commit()
    return todo


@todo_router.get("/{todo_id}")
def read_todo(current_user, todo_id: int, session: Session = Depends(get_session)):
    """
    Get a todo by ID.
    """
    todo = session.query(Todo).filter_by(
        id=todo_id, 
        user_id=current_user.id
    )
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail="Could not find the requested todo."
        )
    return todo


@todo_router.patch("/{todo_id}")
def update_todo(current_user, todo_id: int, data: TodoUpdate, session: Session = Depends(get_session)):
    """
    Update a todo by ID.
    """
    todo = session.query(Todo).filter_by(
        id=todo_id, 
        user_id=current_user.id
    )
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail="Could not find the requested todo."
        )
    if data.content is not None:
        todo.content = data.content
    if data.completed is not None:
        todo.completed = data.completed
    session.add(todo)
    session.commit()
    return todo


@todo_router.delete("/{todo_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_todo(current_user, todo_id: int, session: Session = Depends(get_session)):
    """
    Delete a todo by ID.
    """
    todo = session.query(Todo).filter_by(
        id=todo_id, 
        user_id=current_user.id
    )
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail="Could not find the requested todo."
        )
    session.delete(todo)
    session.commit()


@todo_router.delete("", status_code=HTTPStatus.NO_CONTENT)
def clear_todos(current_user, session: Session = Depends(get_session)):
    """
    Clears the current user's todos.
    """
    todos = session.query(Todo).filter_by(
        user_id=current_user.id
    )
    todos.delete()