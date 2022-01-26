from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.validate import Length


class LoginSchema(Schema):
    email = String(required=True)
    password = String(
        required=True, 
        load_only=True, 
        validate=(
            Length(min=8, max=255)
        ),
    )


login_schema = LoginSchema()