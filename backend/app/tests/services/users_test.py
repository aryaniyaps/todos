from sqlalchemy.orm import Session

from app.models.users import User


def test_user_by_email(session: Session, user: User) -> None:
    """
    Ensure we can get an user by email.
    """
    pass


def test_create_user(session: Session) -> None:
    """
    Ensure we can create an user.
    """
    pass