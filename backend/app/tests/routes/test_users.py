from faker import Faker
from flask import url_for
from flask.testing import FlaskClient


def test_read_current_user(client: FlaskClient) -> None:
    """
    Ensure we can read the current user.
    """
    result = client.get(url_for("app.users.read_current_user"))


def test_create_user(client: FlaskClient, faker: Faker) -> None:
    """
    Ensure we can create an user.
    """
    result = client.post(url_for("app.users.create_user"), data={})