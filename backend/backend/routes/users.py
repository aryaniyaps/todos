from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_required, current_user

from backend.schemas.users import UserSchema
from backend.services.users import create_user, user_by_email


user_blueprint = Blueprint(
    name="users", 
    import_name=__name__, 
    url_prefix="/users",
)


@user_blueprint.get("/me")
@login_required
def read_current_user():
    """
    Get the current user.
    """
    schema = UserSchema()
    return {"user": schema.dump(current_user)}


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
    user = create_user(
        email=data.get("email"),
        password=data.get("password"), 
    )
    return {"user": schema.dump(user)}
