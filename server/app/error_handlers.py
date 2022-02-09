from http import HTTPStatus

from flask.typing import ResponseReturnValue

from app.errors import InvalidAccess, InvalidInput, ResourceNotFound


def invalid_access_handler(error: InvalidAccess) -> ResponseReturnValue:
    """
    Handle invalid access errors.

    :param error: The error to handle.
    """
    return {"message": error.message}, HTTPStatus.FORBIDDEN


def invalid_input_handler(error: InvalidInput) -> ResponseReturnValue:
    """
    Handle invalid input errors.

    :param error: The error to handle.
    """
    return {"message": error.message}, HTTPStatus.BAD_REQUEST


def resource_not_found_handler(error: ResourceNotFound) -> ResponseReturnValue:
    """
    Handle resource not found errors.

    :param error: The error to handle.
    """
    return {"message": error.message}, HTTPStatus.NOT_FOUND