from http import HTTPStatus

from flask import Blueprint, request
from flask.typing import ResponseReturnValue
from flask_login import current_user, login_required, login_user

from app.users.schemas import user_schema, user_create_schema
from app.users.services import UserService


user_blueprint = Blueprint(
    name="users", 
    import_name=__name__, 
    url_prefix="/users",
)


@user_blueprint.get("/@me")
@login_required
def read_current_user() -> ResponseReturnValue:
    """
    Get the current user.
    """
    return user_schema.dump(current_user)


@user_blueprint.post("")
def create_user() -> ResponseReturnValue:
    """
    Create an user.
    """
    data = user_create_schema.load(request.json)
    user = UserService.create_user(
        email=data.get("email"), 
        password=data.get("password"),
    )
    login_user(user=user)
    return user_schema.dump(user), HTTPStatus.CREATED
