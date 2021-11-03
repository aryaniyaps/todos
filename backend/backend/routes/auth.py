from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_user

from backend.services.auth import authenticate_user
from backend.schemas.users import UserSchema


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/login")
def authenticate_user():
    """
    Log the current user in.
    """
    schema = UserSchema()
    data = schema.load(request.get_json())
    user = authenticate_user(
        email=data.get("email"), 
        password=data.get("password"),
    )
    if user is None:
        errors = {
            "errors": "Incorrect email/ password provided."
        }
        return errors, HTTPStatus.BAD_REQUEST
    login_user(user=user)
    return {"user": schema.dump(user)}


@auth_blueprint.post("/password/forgot")
def forgot_password():
    """
    Request a password reset email.
    """
    pass


@auth_blueprint.post("/password/reset")
def reset_password():
    """
    Reset password for the associated user.
    """
    pass
