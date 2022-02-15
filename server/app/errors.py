class BaseError(Exception):
    """
    Base error class.
    """
    def __init__(self, message: str) -> None:
        self.message = message


class InvalidInput(BaseError):
    """
    Indicate that the client has
    issued an invalid request.
    """
    pass


class ResourceNotFound(BaseError):
    """
    Indicate that the requested 
    resource doesn't exist.
    """
    pass


class Unauthenticated(BaseError):
    """
    Indicate that the client has not
    authenticated yet.
    """
    pass
