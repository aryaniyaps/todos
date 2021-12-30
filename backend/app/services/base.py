from sqlalchemy.orm import Session


class BaseService:
    """
    Parent class that must be inherited
    by every service.
    """

    def __init__(self, session: Session) -> None:
        self.session = session
