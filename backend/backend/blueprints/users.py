from flask import Blueprint


user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.get("/me")
async def read_current_user():
    """
    Get the current user.
    """
    pass


@user_blueprint.patch("/me")
async def update_current_user():
    """
    Update the current user.
    """
    pass


@user_blueprint.post("")
async def create_user():
    """
    Create a new user.
    """
    pass
