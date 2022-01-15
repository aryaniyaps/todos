from http import HTTPStatus

from flask import Blueprint

from app.users.entities import User
from app.users.services import user_service


user_blueprint = Blueprint("users", __name__, url_prefix="/users")


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
def create_user(data: UserCreateInput) -> User:
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
