from flask import Blueprint, request
from flask_login import login_required, current_user

from backend.schemas.users import UserSchema
from backend.services.users import create_user, update_user


user_blueprint = Blueprint(
    name="users", 
    import_name=__name__, 
    url_prefix="/users",
)


@user_blueprint.get("/me")
@login_required
def read_current_user():
    """
    Get the current user.
    """
    schema = UserSchema()
    return {"user": schema.dump(current_user)}


@user_blueprint.patch("/me")
@login_required
def update_current_user():
    """
    Update the current user.
    """
    schema = UserSchema()
    data = schema.load(request.get_json())
    user = update_user(
        user=current_user,
        avatar=data.get("avatar")
    )
    return {"user": schema.dump(user)}


@user_blueprint.post("")
def create_user():
    """
    Create a new user.
    """
    schema = UserSchema()
    data = schema.load(request.get_json())
    user = create_user(
        email=data.get("email"),
        password=data.get("password"), 
    )
    return {"user": schema.dump(user)}
