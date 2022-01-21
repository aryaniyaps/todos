from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_required, login_user, logout_user

from app.auth.schemas import login_schema
from app.auth.services import auth_service
from app.users.schemas import user_schema


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/login")
def login():
    data = login_schema.load(request.json)
    user = auth_service.authenticate_user(
        email=data.email, 
        password=data.password,
    )
    login_user(user=user)
    return user_schema.dump(user)


@auth_blueprint.post("/logout")
@login_required
def logout():
    """
    Log the current user out.
    """
    logout_user()
    return "", HTTPStatus.NO_CONTENT
