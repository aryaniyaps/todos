from passlib.hash import bcrypt

from app.users.entities import User
from app.users.repositories import UserRepo


def test_get_user(user: User) -> None:
    """
    Ensure we can get an user by ID.
    """
    result = UserRepo.get_user(user_id=user.id)
    assert result == user


def test_get_unknown_user(user: User) -> None:
    """
    Ensure we cannot get an unknown user by ID.
    """
    UserRepo.delete_user(user=user)
    result = UserRepo.get_user(user_id=user.id)
    assert result is None


def test_get_user_by_email(user: User) -> None:
    """
    Ensure we can get an user by email.
    """
    result = UserRepo.get_user_by_email(email=user.email)
    assert result == user


def test_get_unknown_user_by_email(user: User) -> None:
    """
    Ensure we cannot get an unknown user by email.
    """
    result = UserRepo.get_user_by_email(
        email="unknown-user@example.org",
    )
    assert result is None


def test_create_user() -> None:
    """
    Ensure we can create an user.
    """
    email = "user@example.org"
    password = "password"
    result = UserRepo.create_user(
        email=email,
        password=password
    )
    assert result.email == email
    assert result.password != password
    assert bcrypt.identify(result.password)


def test_delete_user(user: User) -> None:
    """
    Ensure we can delete an user.
    """
    UserRepo.delete_user(user=user)
    result = UserRepo.get_user(user_id=user.id)
    assert result is None