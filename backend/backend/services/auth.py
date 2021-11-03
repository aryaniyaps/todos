from typing import Optional

from backend.models.users import User
from backend.services.users import user_by_email


def authenticate_user(email: str, password: str) -> Optional[User]:
    """
    Checks if the given email/password 
    combination is correct.
    """
    user = user_by_email(email=email)
    authenticated = (
        user is not None and 
        user.check_password(password=password)
    )
    if not authenticated:
        return None
    return user