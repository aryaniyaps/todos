class BaseException(Exception):
    """
    Base Exception class.
    """
    def __init__(self, message: str) -> None:
        self.message = message


class InvalidUsage(BaseException):
    pass


class ResourceNotFound(BaseException):
    """The requested resource doesn't exist."""
    pass