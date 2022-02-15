from http import HTTPStatus

from flask import Blueprint, request, session
from flask.typing import ResponseReturnValue

from app.auth.decorators import auth_required
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
@auth_required
def read_todos() -> ResponseReturnValue:
    """
    Get the current user's todos.
    """
    result = TodoService.get_todos(
        user_id=session["user_id"],
        per_page=request.args.get("per_page"),
        after=request.args.get("after"),
    )
    return {
        "page_meta": result.page_meta,
        "entities": todos_schema.dump(
            result.entities
        ), 
    }


@todo_blueprint.post("")
@auth_required
def create_todo() -> ResponseReturnValue:
    """
    Create a todo.
    """
    data = todo_create_schema.load(request.json)
    result = todo_schema.dump(
        TodoService.create_todo(
            user_id=session["user_id"],
            content=data["content"], 
        ),
    )
    return result, HTTPStatus.CREATED


@todo_blueprint.get("/<int:todo_id>")
@auth_required
def read_todo(todo_id: int) -> ResponseReturnValue:
    """
    Get a todo by ID.
    """
    return todo_schema.dump(
        TodoService.get_todo(
            user_id=session["user_id"],
            todo_id=todo_id, 
        ),
    )


@todo_blueprint.patch("/<int:todo_id>")
@auth_required
def update_todo(todo_id: int) -> ResponseReturnValue:
    """
    Update a todo by ID.
    """
    data = todo_update_schema.load(request.json)
    return todo_schema.dump(
        TodoService.update_todo(
            user_id=session["user_id"],
            todo_id=todo_id, 
            completed=data["completed"], 
            content=data["content"],
        ),
    )


@todo_blueprint.delete("/<int:todo_id>")
@auth_required
def delete_todo(todo_id: int) -> ResponseReturnValue:
    """
    Delete a todo by ID.
    """
    TodoService.delete_todo(
        user_id=session["user_id"], 
        todo_id=todo_id,
    )
    return "", HTTPStatus.NO_CONTENT


@todo_blueprint.delete("")
@auth_required
def clear_todos() -> ResponseReturnValue:
    """
    Clear the current user's todos.
    """
    TodoService.clear_todos(user_id=session["user_id"])
    return "", HTTPStatus.NO_CONTENT
