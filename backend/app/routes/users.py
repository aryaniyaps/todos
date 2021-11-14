from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_required, current_user

from app.extensions import db
from app.models.users import User
from app.schemas.users import user_schema


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
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    if user is not None:
        errors = {
            "errors": {
                "email": "User with email already exists."
            }
        }
        return errors, HTTPStatus.BAD_REQUEST
    user = User(email=email)
    user.set_password(password=password)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), HTTPStatus.CREATED
