from http import HTTPStatus

from sanic import Request
from marshmallow import ValidationError


def handle_validation_error(request: Request, exception: ValidationError):
    """
    Handles validation errors.
    """
    return {"errors": exception.messages}, HTTPStatus.BAD_REQUEST