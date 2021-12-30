from http import HTTPStatus
from typing import Callable, Generator, Type

from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database import session_factory
from app.models.todos import Todo
from app.models.users import User
from app.services.base import BaseService
from backend.app.services.todos import TodoService


def get_session() -> Generator[Session, None, None]:
    session = session_factory()
    try:
        yield session
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


def get_service(
    service: Type[BaseService],
) -> Callable[[Session], BaseService]:
    def service_initializer(
        session: Session = Depends(
            dependency=get_session,
        ),
    ) -> BaseService:
        return service(session=session)
    return service_initializer


def get_current_user() -> User:
    pass


def get_todo(
    todo_id: int, 
    current_user: User = Depends(
        dependency=get_current_user,
    ), 
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
) -> Todo:
    todo = todo_service.get_todo(
        todo_id=todo_id, 
        user_id=current_user.id,
    )
    if todo is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Could not find the requested todo.",
        )
    return todo
