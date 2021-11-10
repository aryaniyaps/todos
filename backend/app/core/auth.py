from typing import Optional

from flask_httpauth import HTTPTokenAuth

from app.core.security import check_auth_token
from app.models.users import User

__all__ = ("auth",)


auth = HTTPTokenAuth()


@auth.verify_token
def verify_auth_token(token) -> Optional[User]:
    return check_auth_token(token=token)