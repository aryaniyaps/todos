from http import HTTPStatus

from flask import Blueprint, request

from app.core.auth import auth
from app.models.users import User
from app.schemas.users import user_schema


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.post("/login")
def login():
    """
    Log the current user in.
    """
    data = user_schema.load(request.get_json())
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    authenticated = (
        user is not None and 
        user.check_password(password=password)
    )
    if not authenticated:
        errors = {
            "errors": "Incorrect email/ password provided."
        }
        return errors, HTTPStatus.BAD_REQUEST
    return {"user": user_schema.dump(user), "token": user.auth_token}


@auth_blueprint.post("/logout")
@auth.login_required
def logout():
    """
    Log the current user out.
    """
    # remove_auth_token(user=auth.current_user())
    return "", HTTPStatus.NO_CONTENT
