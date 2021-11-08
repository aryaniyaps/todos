from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_required, current_user, login_user

from app.core.emails import send_user_created_mail
from app.schemas.users import user_schema
from app.services.users import (
    create_user as _create_user, 
    user_by_email
)


user_blueprint = Blueprint("users",  __name__, url_prefix="/users")


@user_blueprint.get("/me")
@login_required
def read_current_user():
    """
    Get the current user.
    """
    return user_schema.dump(current_user)


@user_blueprint.post("")
def create_user():
    """
    Create a new user.
    """
    data = user_schema.load(request.get_json())
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
    send_user_created_mail(recipient=user.email, user=user)
    login_user(user=user)
    return user_schema.dump(user), HTTPStatus.CREATED
