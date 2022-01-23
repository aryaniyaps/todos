class BaseError(Exception):
    """Base error class."""
    def __init__(self, message: str) -> None:
        self.message = message


class InvalidUsage(BaseError):
    """
    Indicates that the client has
    issued a bad request.
    """
    pass


class ResourceNotFound(BaseError):
    """
    Indicates that the requested 
    resource doesn't exist.
    """
    pass
