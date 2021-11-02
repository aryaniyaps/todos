from flask import Blueprint
from flask_login import login_required


todo_blueprint = Blueprint("todos", __name__, url_prefix="/todos")


@todo_blueprint.get("/{todo_id}")
@login_required
def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    pass


@todo_blueprint.get("")
@login_required
def read_todos():
    """
    Get the current user's todos.
    """
    pass


@todo_blueprint.post("")
@login_required
def create_todo():
    """
    Create a new todo.
    """
    pass


@todo_blueprint.patch("/{todo_id}")
@login_required
def update_todo(todo_id: int):
    """
    Update a todo by ID.
    """
    pass


@todo_blueprint.delete("/{todo_id}")
@login_required
def delete_todo(todo_id: int):
    """
    Delete a todo by ID.
    """
    pass