from http import HTTPStatus

from flask import Blueprint, request

from app.core.auth import auth, generate_auth_token
from app.core.emails import send_user_created_mail
from app.extensions import db
from app.models.users import User
from app.schemas.users import user_schema


user_blueprint = Blueprint("users",  __name__, url_prefix="/users")


@user_blueprint.get("/me")
@auth.login_required
def read_current_user():
    """
    Get the current user.
    """
    return user_schema.dump(auth.current_user())


@user_blueprint.post("")
def create_user():
    """
    Create a new user.
    """
    data = user_schema.load(request.get_json())
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email)
    if user is not None:
        errors = {
            "errors": {
                "email": "User with email already exists."
            }
        }
        return errors, HTTPStatus.BAD_REQUEST
    auth_token = generate_auth_token()
    user = User(email=email, auth_token=auth_token)
    user.set_password(password=password)
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    send_user_created_mail(recipient=user.email, user=user)
    return {"user": user_schema.dump(user), "token": auth_token}, HTTPStatus.CREATED
