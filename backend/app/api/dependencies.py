from http import HTTPStatus
from typing import Generator, Type

from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database import session_factory
from app.models.todos import Todo
from app.models.users import User
from app.services.base import BaseService
from backend.app.services.todos import TodoService


def get_session() -> Generator[Session, None, None]:
    """
    Gets a session instance.

    :return: the obtained session.
    """
    session = session_factory()
    try:
        yield session
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


def get_service(service: Type[BaseService]):
    pass


def get_current_user() -> User:
    pass


def get_todo(
    todo_id: int, 
    current_user: User = Depends(get_current_user), 
    todo_service: TodoService = Depends(get_service(TodoService))
) -> Todo:
    todo = todo_service.get_todo(todo_id=todo_id, user_id=current_user.id)
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Could not find the requested todo.",
        )
    return todo
