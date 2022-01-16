from http import HTTPStatus

from flask import Blueprint
from flask_login import current_user, login_required

from app.todos.entities import Todo
from app.todos.services import todo_service


todo_blueprint = Blueprint(
    name="todos", 
    import_name=__name__, 
    url_prefix="/todos",
)


@todo_blueprint.get("")
@login_required
def read_todos():
    """
    Get the current user's todos.
    """
    return todo_service.get_todos(user_id=current_user.id)


@todo_blueprint.post("")
@login_required
def create_todo():
    """
    Create a new todo.
    """
    todo = todo_service.create_todo(
        content=data.content,  
        user_id=current_user.id,
    )
    return todo, HTTPStatus.CREATED


@todo_blueprint.get("/<todo_id:int>")
@login_required
def read_todo():
    """
    Get a todo by ID.
    """
    return todo


@todo_blueprint.patch("/<todo_id:int>")
@login_required
def update_todo():
    """
    Update a todo by ID.
    """
    return todo_service.update_todo(
        todo=todo, 
        completed=data.completed, 
        content=data.content,
    )


@todo_blueprint.delete("/<todo_id:int>")
@login_required
def delete_todo():
    """
    Delete a todo by ID.
    """
    todo_service.delete_todo(todo=todo)
    return "", HTTPStatus.NO_CONTENT


@todo_blueprint.delete("")
@login_required
def clear_todos():
    """
    Clear the current user's todos.
    """
    todo_service.clear_todos(user_id=current_user.id)
    return "", HTTPStatus.NO_CONTENT
