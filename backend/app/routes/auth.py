from http import HTTPStatus

from sanic import Blueprint, Request
from sanic.response import empty, json

from app.core.auth import login_required
from app.core.database import get_session
from app.models.users import User
from app.schemas.users import user_schema


auth_blueprint = Blueprint("auth", url_prefix="/auth")


@auth_blueprint.post("/login")
def login(request: Request):
    """
    Log the current user in.
    """
    data = user_schema.load(request.json)
    email = data.get("email")
    password = data.get("password")
    with get_session() as session:
        user = session.query(User).filter_by(email=email).first()
    authenticated = (
        user is not None and 
        user.check_password(password=password)
    )
    if not authenticated:
        errors = {
            "errors": "Incorrect email/ password provided."
        }
        return errors, HTTPStatus.BAD_REQUEST
    login_user(user=user)
    return json(user_schema.dump(user))


@auth_blueprint.post("/logout")
@login_required
def logout(request: Request):
    """
    Log the current user out.
    """
    logout_user()
    return empty()
