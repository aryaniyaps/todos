from http import HTTPStatus

from fastapi import APIRouter

from app.core.auth import login_required
from app.core.database import get_session
from app.models.users import User
from app.schemas.users import UserCreate


user_router = APIRouter(prefix="/users")


@user_router.get("/me")
@login_required
def read_current_user():
    """
    Get the current user.
    """
    return current_user


@user_router.post("", status_code=HTTPStatus.CREATED)
def create_user(data: UserCreate):
    """
    Create a new user.
    """
    with get_session() as session:
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
