from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_required, login_user, logout_user

from app.auth.schemas import authenticate_schema
from app.auth.services import auth_service
from app.users.schemas import user_schema


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/authenticate")
def authenticate():
    """
    Authenticate the current user.
    """
    data = authenticate_schema.load(request.json)
    user = auth_service.authenticate(
        email=data.get("email"), 
        password=data.get("password"),
    )
    login_user(user=user)
    return user_schema.dump(user)


@auth_blueprint.post("/unauthenticate")
@login_required
def unauthenticate():
    """
    Unauthenticate the current user.
    """
    logout_user()
    return "", HTTPStatus.NO_CONTENT
