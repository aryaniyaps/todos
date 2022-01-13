from http import HTTPStatus

from flask import Blueprint
from fastapi import Depends
from fastapi.exceptions import HTTPException

from app.api.providers import get_service, get_current_user
from app.entities.users import User
from app.models.users import UserCreateInput, UserModel
from app.services.users import UserService

user_blueprint = Blueprint(url_prefix="/users")


@user_blueprint.get("/@me")
def read_current_user(
    current_user: User = Depends(
        dependency=get_current_user,
    ),
)-> User:
    """
    Get the current user.
    """
    return current_user


@user_blueprint.post("")
def create_user(
    data: UserCreateInput, 
    user_service: UserService = Depends(
        dependency=get_service(
            service=UserService,
        ),
    ),
) -> User:
    """
    Create a new user.
    """
    user = user_service.user_by_email(email=data.email)
    if user is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, 
            detail="User with email already exists.",
        )
    return user_service.create_user(
        email=data.email, 
        password=data.password,
    )
