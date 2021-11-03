from http import HTTPStatus

from marshmallow import ValidationError


def handle_validation_error(error: ValidationError):
    """
    Handles validation errors.
    """
    return {"errors": error.messages}, HTTPStatus.BAD_REQUEST