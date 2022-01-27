from http import HTTPStatus
from typing import Optional

from flask_login import LoginManager

from app.users.entities import User
from app.users.services import user_service


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    """
    Loads an user from the given ID.

    :param user_id: The given ID.

    :return: The user with the given ID.
    """
    return user_service.get_user(user_id=int(user_id))


@login_manager.unauthorized_handler
def unauthorized_handler():
    result = {"message": "Could not validate the given credentials."}
    return result, HTTPStatus.UNAUTHORIZED
