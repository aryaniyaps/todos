from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from app.api.dependencies import get_service, get_current_user
from app.models.users import User
from app.schemas.auth import LoginSchema
from app.services.users import UserService

auth_router = APIRouter(prefix="/auth")


@auth_router.post(path="/login", name="auth:login")
def login(
    data: LoginSchema, 
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
    authenticated = user is not None and user.check_password(password=data.password)
    if not authenticated:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect email/ password provided.",
        )
    # TODO: login user here.
    return user


@auth_router.post(path="/logout", name="auth:logout", status_code=HTTPStatus.NO_CONTENT)
def logout(
    current_user: User = Depends(
        dependency=get_current_user,
    ),
) -> None:
    """
    Log the current user out.
    """
    # TODO: logout user here.
    pass
