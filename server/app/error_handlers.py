from http import HTTPStatus

from flask.typing import ResponseReturnValue

from app.errors import InvalidInput, ResourceNotFound, Unauthenticated


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


def unauthenticated_handler(error: Unauthenticated) -> ResponseReturnValue:
    """
    Handle unauthenticated errors.

    :param error: The error to handle.
    """
    return {"message": error.message}, HTTPStatus.UNAUTHORIZED