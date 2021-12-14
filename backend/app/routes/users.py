from http import HTTPStatus

from sanic import Blueprint, Request
from sanic.response import json
from flask_login import login_required, current_user

from app.core.database import get_session
from app.models.users import User
from app.schemas.users import user_schema


user_blueprint = Blueprint("users", url_prefix="/users")


@user_blueprint.get("/me")
@login_required
def read_current_user(request: Request):
    """
    Get the current user.
    """
    return json(user_schema.dump(current_user))


@user_blueprint.post("")
def create_user(request: Request):
    """
    Create a new user.
    """
    data = user_schema.load(request.get_json())
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    if user is not None:
        errors = {
            "errors": {
                "email": "User with email already exists."
            }
        }
        return json(errors, status=HTTPStatus.BAD_REQUEST)
    user = User(email=email)
    user.set_password(password=password)
    with get_session() as session:
        session.add(user)
        session.commit()
    return json(
        user_schema.dump(user), 
        status=HTTPStatus.CREATED
    )
