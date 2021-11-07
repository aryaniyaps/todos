from http import HTTPStatus

from flask import Blueprint, request

from app.extensions import auth
from app.core.security import create_auth_token
from app.schemas.users import UserSchema
from app.services.users import (
    create_user as _create_user, 
    user_by_email
)


user_blueprint = Blueprint("users",  __name__, url_prefix="/users")


@user_blueprint.get("/me")
@auth.login_required
def read_current_user():
    """
    Get the current user.
    """
    return UserSchema().dump(auth.current_user())


@user_blueprint.post("")
def create_user():
    """
    Create a new user.
    """
    schema = UserSchema()
    data = schema.load(request.get_json())
    user = user_by_email(email=data.get("email"))
    if user is not None:
        errors = {
            "errors": {
                "email": "User with email already exists."
            }
        }
        return errors, HTTPStatus.BAD_REQUEST
    user = _create_user(
        email=data.get("email"),
        password=data.get("password"), 
    )
    token = create_auth_token(user_id=user.id)
    return {"token": token, "user": schema.dump(user)}, HTTPStatus.CREATED
