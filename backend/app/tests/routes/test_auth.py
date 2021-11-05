from flask import url_for
from flask.testing import FlaskClient


def test_authenticate_user(client: FlaskClient) -> None:
    """
    Ensure we can log the current user in.
    """
    response = client.post(url_for("app.auth.authenticate_user"), json={})


def test_unauthenticate_user(client: FlaskClient) -> None:
    """
    Ensure we can log the current user out.
    """
    response = client.post(url_for("app.auth.unauthenticate_user"))