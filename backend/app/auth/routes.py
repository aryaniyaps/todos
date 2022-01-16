from http import HTTPStatus

from flask import Blueprint

from app.users.entities import User
from app.users.services import user_service


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/login")
def login() -> User:
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
    # TODO: login user.
    return user


@auth_blueprint.post("/logout")
def logout() -> None:
    """
    Log the current user out.
    """
    # TODO: logout user.
    pass
