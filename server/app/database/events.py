from app.database.core import db_session


def shutdown_session(exception=None) -> None:
    """
    Shuts down the database session.
    """
    db_session.remove()