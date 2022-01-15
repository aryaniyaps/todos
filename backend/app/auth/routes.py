from http import HTTPStatus
from typing import Optional

from flask import Blueprint

from app.users.entities import User
from app.auth.services import auth_service
from app.users.services import user_service


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.post("/login")
def login(
    data: LoginInput, 
    response: Response,
) -> User:
    """
    Log the current user in.
    """
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
    access_token = auth_service.create_access_token(user=user)
    response.set_cookie(
        key="access_token", 
        value=access_token, 
        httponly=True, 
        samesite="Strict",
    )
    return user


@auth_blueprint.post("/logout")
def logout(
    response: Response,
    access_token: Optional[str] = Cookie(None),
) -> None:
    """
    Log the current user out.
    """
    auth_service.revoke_access_token(
        access_token=access_token,
    )
    response.delete_cookie(key="access_token")
