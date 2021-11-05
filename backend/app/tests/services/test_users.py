from faker import Faker

from app.models.users import User
from app.services.users import (
    create_user, 
    deactivate_user, 
    load_user, 
    user_by_email
)


def test_create_user(faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    email = faker.ascii_safe_email()
    password = faker.password(length=12)
    user = create_user(
        email=email,
        password=password
    )
    assert user.is_active
    assert user.check_password(password)
    assert user.email == email


def test_deactivate_user(faker: Faker) -> None:
    """
    Ensure we can deactivate an user.
    """
    user = create_user(
        email=faker.ascii_safe_email(),
        password=faker.password(length=12)
    )
    user = deactivate_user(user=user)
    assert not user.is_active


def test_load_user(test_user: User) -> None:
    """
    Ensure we can load an user by their ID.
    """
    user = load_user(user_id=test_user.id)
    assert user == test_user
    unknown_user = load_user(user_id="unknown")
    assert unknown_user is None


def test_user_by_email(test_user: User) -> None:
    """
    Ensure we can load an user by their email.
    """
    user = user_by_email(email=test_user.email)
    assert user == test_user
    unknown_user = user_by_email(email="unknown@example.org")
    assert unknown_user is None