class BaseException(Exception):
    """
    Base Exception class.
    """
    def __init__(self, message: str) -> None:
        self.message = message


class InvalidUsage(BaseException):
    """
    Used to indicate that the client has
    issued a bad request.
    """
    pass


class ResourceNotFound(BaseException):
    """
    Used to indicate that the requested 
    resource doesn't exist.
    """
    pass