from http import HTTPStatus

from fastapi import APIRouter

from app.core.auth import login_required
from app.core.database import get_session
from app.models.todos import Todo
from app.schemas.todos import TodoCreate


todo_router = APIRouter(prefix="/todos")


@todo_router.get("")
@login_required
def read_todos(offset: int = 1, limit: int = 20):
    """
    Get the current user's todos.
    """
    with get_session() as session:
        todos = session.query(Todo).filter_by(user_id=current_user.id)
        todos.offset(offset).limit(limit)
    return todos


@todo_router.post("", status_code=HTTPStatus.CREATED)
@login_required
def create_todo(data: TodoCreate):
    """
    Create a new todo.
    """
    with get_session() as session:
        todo = Todo(
            content=data.content, 
            completed=data.completed,
            user_id=current_user.id
        )
        session.add(todo)
        session.commit()
    return todo


@todo_router.get("/{todo_id}")
@login_required
def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    with get_session() as session:
        todo = session.query(Todo).filter_by(
            id=todo_id, 
            user_id=current_user.id
        )
    if todo is None:
        raise NotFound("Couldn't find the requested todo.")
    return todo


@todo_router.patch("/{todo_id}")
@login_required
def update_todo(todo_id: int):
    """
    Update a todo by ID.
    """
    with get_session() as session:
        todo = session.query(Todo).filter_by(
            id=todo_id, 
            user_id=current_user.id
        )
        if todo is None:
            raise NotFound("Couldn't find the requested todo.")
        data = todo_schema.load()
        content = data.get("content")
        completed = data.get("completed")
        if content is not None:
            todo.content = content
        if completed is not None:
            todo.completed = completed
        session.add(todo)
        session.commit()
    return todo_schema.dump(todo)


@todo_router.delete("/{todo_id}", status_code=HTTPStatus.NO_CONTENT)
@login_required
def delete_todo(todo_id: int):
    """
    Delete a todo by ID.
    """
    with get_session() as session:
        todo = session.query(Todo).filter_by(
            id=todo_id, 
            user_id=current_user.id
        )
        if todo is None:
            raise NotFound("Couldn't find the requested todo.")
        session.delete(todo)
        session.commit()


@todo_router.delete("", status_code=HTTPStatus.NO_CONTENT)
@login_required
def clear_todos():
    """
    Clears the current user's todos.
    """
    with get_session() as session:
        todos = session.query(Todo).filter_by(
            user_id=current_user.id
        )
        todos.delete()