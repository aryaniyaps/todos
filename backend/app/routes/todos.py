from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.services.todos import TodoService
from app.models.todos import Todo
from app.models.users import User
from app.schemas.todos import TodoCreate, TodoUpdate


todo_router = APIRouter(prefix="/todos")


def get_todo(current_user: User, todo_id: int, session: Session = Depends(get_session)) -> Todo:
    todo = TodoService(session).get_todo(
        todo_id=todo_id, 
        user_id=current_user.id
    )
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail="Could not find the requested todo."
        )
    return todo



@todo_router.get("", name="todos:read-all")
def read_todos(
    current_user: User, 
    session: Session = Depends(get_session)
):
    """
    Get the current user's todos.
    """
    return TodoService(session).get_todos(user_id=current_user.id)


@todo_router.post("", name="todos:create", status_code=HTTPStatus.CREATED)
def create_todo(
    current_user: User, 
    data: TodoCreate, 
    session: Session = Depends(get_session)
):
    """
    Create a new todo.
    """
    return TodoService(session).create_todo(
        content=data.content,
        completed=data.completed,
        user_id=current_user.id
    )


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
    return TodoService(session).update_todo(
        todo=todo,
        completed=data.completed,
        content=data.content
    )


@todo_router.delete("/{todo_id}", name="todos:delete", status_code=HTTPStatus.NO_CONTENT)
def delete_todo(
    todo: Todo = Depends(get_todo), 
    session: Session = Depends(get_session)
):
    """
    Delete a todo by ID.
    """
    TodoService(session).delete_todo(todo=todo)


@todo_router.delete("", name="todos:clear", status_code=HTTPStatus.NO_CONTENT)
def clear_todos(
    current_user: User, 
    session: Session = Depends(get_session)
):
    """
    Clears the current user's todos.
    """
    TodoService(session).clear_todos(user_id=current_user.id)