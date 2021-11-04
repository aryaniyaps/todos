from typing import Optional

from app.extensions import db
from app.models.users import User


def load_user(user_id: int) -> Optional[User]:
    """
    Loads an user by their ID.
    """
    return User.query.filter(User.id == user_id).first()

def user_by_email(email: str) -> Optional[User]:
    """
    Gets an user by their email.
    """
    return User.query.filter(User.email == email).first()


def create_user(
    email: str, 
    password: str,
) -> User:
    """
    Creates a new user.
    """
    user = User(email=email)
    user.set_password(password=password)
    db.session.add(instance=user)
    db.session.commit()
    db.session.refresh(instance=user)
    return user


def deactivate_user(user: User) -> User:
    """
    Deactivates the given user.
    """
    user.is_active = False
    db.session.add(instance=user)
    db.session.commit()
    db.session.refresh(instance=user)
    return user