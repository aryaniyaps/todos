from http import HTTPStatus

from fastapi import APIRouter, Request, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import Login
from app.core.database import get_session
from app.models.users import User


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", name="auth:login")
def login(request: Request, data: Login, session: Session = Depends(get_session)):
    """
    Log the current user in.
    """
    user = session.query(User).filter_by(email=data.email).first()
    authenticated = (
        user is not None and 
        user.check_password(password=data.password)
    )
    if not authenticated:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, 
            detail="Incorrect email/ password provided."
        )
    request.session["user_id"] = user.id
    return user


@auth_router.post("/logout", name="auth:logout", status_code=HTTPStatus.NO_CONTENT)
def logout(request: Request, current_user: User):
    """
    Log the current user out.
    """
    del request.session["user_id"]
