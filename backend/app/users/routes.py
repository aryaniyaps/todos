from http import HTTPStatus

from flask import Blueprint

from app.users.entities import User
from app.users.services import user_service


user_blueprint = Blueprint(
    name="users", 
    import_name=__name__, 
    url_prefix="/users",
)


@user_blueprint.get("/@me")
def read_current_user()-> User:
    return current_user


@user_blueprint.post("")
def create_user() -> User:
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
