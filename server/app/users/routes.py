from http import HTTPStatus

from flask import Blueprint, request, session
from flask.typing import ResponseReturnValue

from app.auth.decorators import auth_required
from app.users.schemas import user_schema, user_create_schema
from app.users.services import UserService


user_blueprint = Blueprint(
    name="users", 
    import_name=__name__, 
    url_prefix="/users",
)


@user_blueprint.get("/@me")
@auth_required
def read_current_user() -> ResponseReturnValue:
    """
    Get the current user.
    """
    return user_schema.dump(
        UserService.get_user(
            user_id=session["user_id"],
        ),
    )


@user_blueprint.post("")
def create_user() -> ResponseReturnValue:
    """
    Create an user.
    """
    data = user_create_schema.load(request.json)
    user = UserService.create_user(
        email=data["email"], 
        password=data["password"],
    )
    session["user_id"] = user.id
    return user_schema.dump(user), HTTPStatus.CREATED
