from http import HTTPStatus

from flask.typing import ResponseReturnValue
from flask_login import LoginManager

from app.users.entities import User
from app.users.repositories import UserRepo


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """
    Load an user from the given ID.

    :param user_id: The given ID.

    :return: The user with the given ID.
    """
    return UserRepo.get_user(user_id=int(user_id))


@login_manager.unauthorized_handler
def unauthorized_handler() -> ResponseReturnValue:
    """
    Handle unauthorized responses.
    """
    result = {"message": "Could not validate credentials."}
    return result, HTTPStatus.UNAUTHORIZED
