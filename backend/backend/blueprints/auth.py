from flask import Blueprint


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.post("/login")
async def login():
    """
    Log the current user in.
    """
    pass


@auth_blueprint.post("/password/forgot")
async def forgot_password():
    """
    Request a password reset email.
    """
    pass


@auth_blueprint.post("/password/reset")
async def reset_password():
    """
    Reset password for the associated user.
    """
    pass
