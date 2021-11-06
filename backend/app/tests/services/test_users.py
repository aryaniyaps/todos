from faker import Faker

from app.models.users import User
from app.services.users import create_user, deactivate_user, load_user, user_by_email


def test_create_user(faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    email = faker.ascii_free_email()
    password = faker.password(length=12)
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


def test_load_user(user: User) -> None:
    """
    Ensure we can load an user by their ID.
    """
    loaded_user = load_user(user_id=user.id)
    assert loaded_user == user


def test_user_by_email(user: User) -> None:
    """
    Ensure we can load an user by their email.
    """
    loaded_user = user_by_email(email=user.email)
    assert loaded_user == user