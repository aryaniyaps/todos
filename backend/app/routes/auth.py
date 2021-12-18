from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.users import User


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", name="auth:login")
def login(data, session: Session = Depends(get_session)):
    """
    Log the current user in.
    """
    user = session.query(User).filter_by(email=data.email).first()
    authenticated = (
        user is not None and 
        user.check_password(password=data.password)
    )
    if not authenticated:
        errors = {
            "errors": "Incorrect email/ password provided."
        }
        return errors, HTTPStatus.BAD_REQUEST
    # login_user(user=user)
    return user


@auth_router.post("/logout", name="auth:logout", status_code=HTTPStatus.NO_CONTENT)
def logout():
    """
    Log the current user out.
    """
    pass
