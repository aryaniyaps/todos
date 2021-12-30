from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.users import User
from app.services.users import UserService
from app.schemas.users import UserCreate


user_router = APIRouter(prefix="/users")


@user_router.get("/me", name="users:current")
def read_current_user(current_user: User):
    """
    Get the current user.
    """
    return current_user


@user_router.post("", name="users:create", status_code=HTTPStatus.CREATED)
def create_user(data: UserCreate, session: Session = Depends(get_session)):
    """
    Create a new user.
    """
    user = UserService(session).user_by_email(email=data.email)
    if user is not None:
        errors = {
            "errors": {
                "email": "User with email already exists."
            }
        }
        return errors, HTTPStatus.BAD_REQUEST
    return UserService(session).create_user(
        email=data.email, 
        password=data.password
    )
