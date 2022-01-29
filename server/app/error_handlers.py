from http import HTTPStatus
from typing import Tuple, Dict

from app.errors import InvalidInput, ResourceNotFound


def invalid_input_handler(
    error: InvalidInput,
) -> Tuple[Dict[str, str], HTTPStatus]:
    """Handles invalid input errors."""
    return {"message": error.message}, HTTPStatus.BAD_REQUEST


def resource_not_found_handler(
    error: ResourceNotFound,
) -> Tuple[Dict[str, str], HTTPStatus]:
    """Handles resource not found errors."""
    return {"message": error.message}, HTTPStatus.NOT_FOUND