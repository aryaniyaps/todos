from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models.users import User


def load_user(user_id: int):
    """
    Loads an user by the given ID.
    """
    return User.query.filter(User.id == user_id).first()

def user_by_email(session: Session, email: str) -> Optional[User]:
    """
    Gets an user by their email.
    """
    query = select(User).filter(User.email == email)
    return session.execute(query).scalar_one()


def create_user(
    session: Session,
    email: str, 
    password: str,
) -> User:
    """
    Creates a new user.
    """
    user = User(email=email)
    user.set_password(password=password)
    session.add(instance=user)
    session.commit()
    session.refresh(instance=user)
    return user


def deactivate_user(session: Session, user: User) -> User:
    """
    Deactivates the given user.
    """
    user.is_active = False
    session.add(instance=user)
    session.commit()
    session.refresh(instance=user)
    return user
