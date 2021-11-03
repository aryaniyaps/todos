from flask import Blueprint


auth_blueprint = Blueprint(
    name="auth", 
    import_name=__name__, 
    url_prefix="/auth",
)


@auth_blueprint.post("/login")
def login():
    """
    Log the current user in.
    """
    pass


@auth_blueprint.post("/password/forgot")
def forgot_password():
    """
    Request a password reset email.
    """
    pass


@auth_blueprint.post("/password/reset")
def reset_password():
    """
    Reset password for the associated user.
    """
    pass
