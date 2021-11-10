from flask_httpauth import HTTPTokenAuth

from app.core.security import check_auth_token

__all__ = ("auth",)


auth = HTTPTokenAuth()
auth.verify_token(check_auth_token)