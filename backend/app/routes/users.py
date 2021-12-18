from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.users import User
from app.schemas.users import UserCreate


user_router = APIRouter(prefix="/users")


@user_router.get("/me", name="users:current")
def read_current_user(current_user):
    """
    Get the current user.
    """
    return current_user


@user_router.post("", name="users:create", status_code=HTTPStatus.CREATED)
def create_user(data: UserCreate, session: Session = Depends(get_session)):
    """
    Create a new user.
    """
    user = session.query(User).filter_by(email=data.email).first()
    if user is not None:
        errors = {
            "errors": {
                "email": "User with email already exists."
            }
        }
        return errors, HTTPStatus.BAD_REQUEST
    user = User(email=data.email)
    user.set_password(password=data.password)
    session.add(user)
    session.commit()
    return user
