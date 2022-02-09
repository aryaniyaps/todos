from http import HTTPStatus

from flask_login import LoginManager

from app.users.entities import User
from app.users.repositories import user_repo


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """
    Load an user from the given ID.

    :param user_id: The given ID.

    :return: The user with the given ID.
    """
    return user_repo.by_id(user_id=int(user_id))


@login_manager.unauthorized_handler
def unauthorized_handler():
    """
    Handle unauthorized responses.
    """
    result = {"message": "Could not validate the given credentials."}
    return result, HTTPStatus.UNAUTHORIZED
