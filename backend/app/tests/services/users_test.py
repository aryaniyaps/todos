from app.models.users import User
from app.services.users import (
    create_user, 
    deactivate_user,
    user_by_email
)


def test_create_user() -> None:
    """
    Ensure we can create an user.
    """
    email = "user@example.org"
    password = "password"
    user = create_user(
        email=email, 
        password=password,
    )
    assert user.email == email
    assert user.check_password(password=password)
    assert user.is_active


def test_deactivate_user(user: User) -> None:
    """
    Ensure we can deactivate an user.
    """
    user = deactivate_user(user=user)
    assert not user.is_active


def test_user_by_email(user: User) -> None:
    """
    Ensure we can load an user by their email.
    """
    loaded_user = user_by_email(email=user.email)
    assert loaded_user == user