from flask.testing import FlaskClient


def test_authenticate_user(client: FlaskClient) -> None:
    """
    Ensure we can log the current user in.
    """
    pass


def test_unauthenticate_user(client: FlaskClient) -> None:
    """
    Ensure we can log the current user out.
    """
    pass