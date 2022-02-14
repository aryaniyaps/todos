from http import HTTPStatus

from flask import Blueprint, request
from flask.typing import ResponseReturnValue
from flask_login import login_required, login_user, logout_user

from app.auth.schemas import authenticate_schema
from app.auth.services import AuthService
from app.users.schemas import user_schema


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/authenticate")
def authenticate() -> ResponseReturnValue:
    """
    Authenticate the current user.
    """
    data = authenticate_schema.load(request.json)
    user = AuthService.authenticate(
        email=data.get("email"), 
        password=data.get("password"),
    )
    login_user(user=user)
    return user_schema.dump(user)


@auth_blueprint.post("/unauthenticate")
@login_required
def unauthenticate() -> ResponseReturnValue:
    """
    Unauthenticate the current user.
    """
    logout_user()
    return "", HTTPStatus.NO_CONTENT
