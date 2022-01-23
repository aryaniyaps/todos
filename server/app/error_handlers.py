from http import HTTPStatus

from app.exceptions import InvalidUsage, ResourceNotFound


def handle_invalid_usage(exception: InvalidUsage):
    return {"message": exception.message}, HTTPStatus.BAD_REQUEST


def handle_resource_not_found(exception: ResourceNotFound):
    return {"message": exception.message}, HTTPStatus.NOT_FOUND