from http import HTTPStatus

from sanic import Request
from sanic.response import json
from marshmallow import ValidationError


def handle_validation_error(request: Request, exception: ValidationError):
    """
    Handles validation errors.
    """
    return json({"errors": exception.messages}, status=HTTPStatus.BAD_REQUEST)