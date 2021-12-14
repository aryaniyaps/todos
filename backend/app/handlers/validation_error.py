from http import HTTPStatus

from sanic import Request
from sanic.response import json
from marshmallow import ValidationError


def validation_error_handler(request: Request, exception: ValidationError):
    """Handler for validation errors."""
    return json({"errors": exception.messages}, status=HTTPStatus.BAD_REQUEST)