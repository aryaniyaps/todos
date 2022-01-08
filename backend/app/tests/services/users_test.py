from passlib.hash import argon2
from sqlalchemy.orm import Session

from app.entities.users import User
from app.services.users import UserService


def test_user_by_email(session: Session, user: User) -> None:
    """
    Ensure we can get an user by email.
    """
    result = UserService(session).user_by_email(email=user.email)
    assert result == user


def test_create_user(session: Session) -> None:
    """
    Ensure we can create an user.
    """
    email = "tester@abc.com"
    password = "avocados"
    result = UserService(session).create_user(
        email=email,
        password=password
    )
    assert result.email == email
    assert result.password != password
    assert result.check_password(password)
    assert argon2.identify(result.password)
