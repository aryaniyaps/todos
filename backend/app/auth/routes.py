from http import HTTPStatus

from flask import Blueprint
from flask_login import login_required, login_user, logout_user

from app.users.services import user_service


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/login")
def login():
    user = user_service.user_by_email(email=data.email)
    authenticated = (
        user is not None and 
        user.check_password(password=data.password)
    )
    if not authenticated:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect email/ password provided.",
        )
    login_user(user=user)
    return user


@auth_blueprint.post("/logout")
@login_required
def logout():
    """
    Log the current user out.
    """
    logout_user()
    return "", HTTPStatus.NO_CONTENT
