from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.validate import Length


class AuthenticateSchema(Schema):
    email = String(required=True)
    password = String(
        required=True, 
        load_only=True, 
        validate=(
            Length(min=8, max=255)
        ),
    )


authenticate_schema = AuthenticateSchema()