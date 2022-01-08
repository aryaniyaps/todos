from http import HTTPStatus
from typing import Callable, Generator, Type

from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database import session_factory
from app.entities.todos import Todo
from app.entities.users import User
from app.services.base import BaseService
from backend.app.services.todos import TodoService


def get_session() -> Generator[Session, None, None]:
    """
    Gets a database session, and 
    closes it when it's returned back.

    :return: The datbase session.
    """
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
    """
    Creates the given service.

    :param service: The service to create.

    :return: The created service.
    """
    def create_service(
        session: Session = Depends(
            dependency=get_session,
        ),
    ) -> BaseService:
        """
        Initializes the given service with
        a database session.

        :return: The initialized service.
        """
        return service(session=session)
    return create_service


def get_current_user() -> User:
    """
    Gets the current user from the given request.

    :return: The request's current user.
    """
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
    """
    Gets the associated todo from
    the route's path parameter.

    :return: The fetched todo.
    """
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
