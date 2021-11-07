from http import HTTPStatus

from flask import Blueprint, request

from app.core.security import remove_auth_token
from app.extensions import auth
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
    # TODO: return auth token here.
    return schema.dump(user)


@auth_blueprint.post("/logout")
@auth.login_required
def logout():
    """
    Log the current user out.
    """
    remove_auth_token(user=auth.current_user())
    return "", HTTPStatus.NO_CONTENT
