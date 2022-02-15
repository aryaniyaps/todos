from http import HTTPStatus

from flask import Blueprint, request, session
from flask.typing import ResponseReturnValue

from app.auth.decorators import auth_required
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
    session["user_id"] = user.id
    return user_schema.dump(user)


@auth_blueprint.post("/unauthenticate")
@auth_required
def unauthenticate() -> ResponseReturnValue:
    """
    Unauthenticate the current user.
    """
    del session["user_id"]
    return "", HTTPStatus.NO_CONTENT
