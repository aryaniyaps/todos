from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask.typing import ResponseReturnValue
from flask_login import current_user, login_required

from app.todos.schemas import (
    todo_schema, 
    todo_create_schema, 
    todo_update_schema,
    todos_schema, 
)
from app.todos.services import TodoService


todo_blueprint = Blueprint(
    name="todos", 
    import_name=__name__, 
    url_prefix="/todos",
)


@todo_blueprint.get("")
@login_required
def read_todos() -> ResponseReturnValue:
    """
    Get the current user's todos.
    """
    result = todos_schema.dump(
        TodoService.get_todos(
            user_id=current_user.id,
            per_page=request.args.get("per_page"),
            after=request.args.get("after"),
        )
    )
    return jsonify(result)


@todo_blueprint.post("")
@login_required
def create_todo() -> ResponseReturnValue:
    """
    Create a todo.
    """
    data = todo_create_schema.load(request.json)
    result = todo_schema.dump(
        TodoService.create_todo(
            user_id=current_user.id,
            content=data.get("content"), 
        )
    )
    return result, HTTPStatus.CREATED


@todo_blueprint.get("/<int:todo_id>")
@login_required
def read_todo(todo_id: int) -> ResponseReturnValue:
    """
    Get a todo by ID.
    """
    return todo_schema.dump(
        TodoService.get_todo(
            user_id=current_user.id,
            todo_id=todo_id, 
        )
    )


@todo_blueprint.patch("/<int:todo_id>")
@login_required
def update_todo(todo_id: int) -> ResponseReturnValue:
    """
    Update a todo by ID.
    """
    data = todo_update_schema.load(request.json)
    return todo_schema.dump(
        TodoService.update_todo(
            user_id=current_user.id,
            todo_id=todo_id, 
            completed=data.get("completed"), 
            content=data.get("content"),
        )
    )


@todo_blueprint.delete("/<int:todo_id>")
@login_required
def delete_todo(todo_id: int) -> ResponseReturnValue:
    """
    Delete a todo by ID.
    """
    TodoService.delete_todo(
        user_id=current_user.id, 
        todo_id=todo_id,
    )
    return "", HTTPStatus.NO_CONTENT


@todo_blueprint.delete("")
@login_required
def clear_todos() -> ResponseReturnValue:
    """
    Clear the current user's todos.
    """
    TodoService.clear_todos(user_id=current_user.id)
    return "", HTTPStatus.NO_CONTENT
