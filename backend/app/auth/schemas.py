from marshmallow import Schema
from marshmallow.fields import String


class LoginSchema(Schema):
    email = String(required=True)
    password = String(required=True, load_only=True)
