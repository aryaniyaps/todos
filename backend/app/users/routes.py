from http import HTTPStatus

from flask import Blueprint, request
from flask_login import current_user, login_required, login_user

from app.users.schemas import user_schema, user_create_schema
from app.users.services import user_service


user_blueprint = Blueprint(
    name="users", 
    import_name=__name__, 
    url_prefix="/users",
)


@user_blueprint.get("/@me")
@login_required
def read_current_user():
    return user_schema.dump(current_user)


@user_blueprint.post("")
def create_user():
    data = user_create_schema.load(request.json)
    user = user_service.create_user(
        email=data.email, 
        password=data.password,
    )
    login_user(user=user)
    return user_schema.dump(user), HTTPStatus.CREATED
