from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_user, logout_user, login_required

from app.services.auth import authenticate_user
from app.schemas.users import UserSchema


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.post("/login")
def login():
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
    return schema.dump(user)


@auth_blueprint.post("/logout")
@login_required
def logout():
    """
    Log the current user out.
    """
    logout_user()
    return "", HTTPStatus.NO_CONTENT
