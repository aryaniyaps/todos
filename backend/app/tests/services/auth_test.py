from app.models.users import User
from app.services.auth import authenticate_user


def test_authenticate_user(user: User) -> None:
    """
    Ensure we can authenticate an user.
    """
    pass