from flask import Blueprint
from flask_login import login_required


user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.get("/me")
@login_required
def read_current_user():
    """
    Get the current user.
    """
    pass


@user_blueprint.patch("/me")
@login_required
def update_current_user():
    """
    Update the current user.
    """
    pass


@user_blueprint.post("")
def create_user():
    """
    Create a new user.
    """
    pass
