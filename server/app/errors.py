class BaseError(Exception):
    """
    Base error class.
    """
    def __init__(self, message: str) -> None:
        self.message = message


class InvalidUsage(BaseError):
    """
    Used to indicate that the client has
    issued a bad request.
    """
    pass


class ResourceNotFound(BaseError):
    """
    Used to indicate that the requested 
    resource doesn't exist.
    """
    pass