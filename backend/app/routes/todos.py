from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.todos import Todo
from app.schemas.todos import TodoCreate, TodoUpdate


todo_router = APIRouter(prefix="/todos")


def get_todo(current_user, todo_id: int, session: Session = Depends(get_session)) -> Todo:
    query = session.query(Todo)
    query.filter_by(id=todo_id, user_id=current_user.id)
    todo = query.first()
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail="Could not find the requested todo."
        )
    return todo



@todo_router.get("", name="todos:read-all")
def read_todos(
    current_user, 
    session: Session = Depends(get_session), 
    offset: int = 1, 
    limit: int = 20
):
    """
    Get the current user's todos.
    """
    todos = session.query(Todo).filter_by(user_id=current_user.id)
    todos.offset(offset).limit(limit)
    return todos


@todo_router.post("", name="todos:create", status_code=HTTPStatus.CREATED)
def create_todo(
    current_user, 
    data: TodoCreate, 
    session: Session = Depends(get_session)
):
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


@todo_router.get("/{todo_id}", name="todos:read")
def read_todo(todo: Todo = Depends(get_todo)):
    """
    Get a todo by ID.
    """
    return todo


@todo_router.patch("/{todo_id}", name="todos:update")
def update_todo(
    data: TodoUpdate, 
    todo: Todo = Depends(get_todo), 
    session: Session = Depends(get_session)
):
    """
    Update a todo by ID.
    """
    if data.content is not None:
        todo.content = data.content
    if data.completed is not None:
        todo.completed = data.completed
    session.add(todo)
    session.commit()
    return todo


@todo_router.delete("/{todo_id}", name="todos:delete", status_code=HTTPStatus.NO_CONTENT)
def delete_todo(
    todo: Todo = Depends(get_todo), 
    session: Session = Depends(get_session)
):
    """
    Delete a todo by ID.
    """
    session.delete(todo)
    session.commit()


@todo_router.delete("", name="todos:clear", status_code=HTTPStatus.NO_CONTENT)
def clear_todos(
    current_user, 
    session: Session = Depends(get_session)
):
    """
    Clears the current user's todos.
    """
    todos = session.query(Todo).filter_by(
        user_id=current_user.id
    )
    todos.delete()