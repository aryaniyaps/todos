from app.users.entities import User
from app.users.repositories import user_repo


def test_get_user(user: User) -> None:
    """
    Ensure we can get an user by ID.
    """
    result = user_repo.get_user(user_id=user.id)
    assert result == user


def test_get_user_by_email(user: User) -> None:
    """
    Ensure we can get an user by email.
    """
    result = user_repo.get_user_by_email(email=user.email)
    assert result == user
