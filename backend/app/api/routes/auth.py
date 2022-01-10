from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Cookie, Depends, Response
from fastapi.exceptions import HTTPException

from app.api.providers import get_service
from app.entities.users import User
from app.models.users import UserModel
from app.models.auth import LoginInput
from app.services.auth import AuthService
from app.services.users import UserService

auth_router = APIRouter(prefix="/auth", tags=["authentication"])


@auth_router.post(
    path="/login", 
    name="auth:login", 
    response_model=UserModel,
)
def login(
    data: LoginInput, 
    response: Response,
    auth_service: AuthService = Depends(
        dependency=get_service(
            service=AuthService,
        ),
    ),
    user_service: UserService = Depends(
        dependency=get_service(
            service=UserService,
        ),
    ),
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


@auth_router.post(
    path="/logout", 
    name="auth:logout", 
    status_code=HTTPStatus.NO_CONTENT,
)
def logout(
    response: Response,
    access_token: Optional[str] = Cookie(None),
    auth_service: AuthService = Depends(
        dependency=get_service(
            service=AuthService,
        ),
    ),
) -> None:
    """
    Log the current user out.
    """
    auth_service.revoke_access_token(
        access_token=access_token,
    )
    response.delete_cookie(key="access_token")
