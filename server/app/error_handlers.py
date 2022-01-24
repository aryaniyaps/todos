from http import HTTPStatus

from app.errors import InvalidInput, ResourceNotFound


def invalid_input_handler(exception: InvalidInput):
    """Handles invalid input exceptions."""
    return {"message": exception.message}, HTTPStatus.BAD_REQUEST


def resource_not_found_handler(exception: ResourceNotFound):
    """Handles resource not found exceptions."""
    return {"message": exception.message}, HTTPStatus.NOT_FOUND