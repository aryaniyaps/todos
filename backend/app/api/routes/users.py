from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from app.api.dependencies import get_service, get_current_user
from app.models.users import User
from app.schemas.users import UserCreateSchema, UserSchema
from app.services.users import UserService

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get(
    path="/@me", 
    name="users:current", 
    response_model=UserSchema,
)
def read_current_user(
    current_user: User = Depends(
        dependency=get_current_user,
    ),
)-> User:
    """
    Get the current user.
    """
    return current_user


@user_router.post(
    path="", 
    name="users:create", 
    status_code=HTTPStatus.CREATED, 
    response_model=UserSchema,
)
def create_user(
    data: UserCreateSchema, 
    user_service: UserService = Depends(
        dependency=get_service(
            service=UserService,
        ),
    ),
) -> User:
    """
    Create a new user.
    """
    user = user_service.user_by_email(email=data.email)
    if user is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, 
            detail="User with email already exists.",
        )
    return user_service.create_user(
        email=data.email, 
        password=data.password,
    )