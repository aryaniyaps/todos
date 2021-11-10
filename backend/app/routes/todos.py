from http import HTTPStatus

from flask import Blueprint, request

from app.core.auth import auth
from app.models.todos import Todo
from app.schemas.todos import todo_schema, todos_schema
from app.services.todos import (
    create_todo as _create_todo, 
    delete_todo as _delete_todo, 
    update_todo as _update_todo,
    clear_todos as _clear_todos
)


todo_blueprint = Blueprint("todos", __name__, url_prefix="/todos")


@todo_blueprint.get("")
@auth.login_required
def read_todos():
    """
    Get the current user's todos.
    """
    query = Todo.query.filter_by(user_id=auth.current_user().id)
    page = request.args.get(key="page", default=1, type=int)
    limit = request.args.get(key="limit", default=20, type=int)
    results = query.paginate(
        page=page, 
        per_page=limit, 
        error_out=False,
    )
    return {
        "results": todos_schema.dump(results.items),
        "has_prev": results.has_prev,
        "has_next": results.has_next,
        "count": results.total
    }


@todo_blueprint.post("")
@auth.login_required
def create_todo():
    """
    Create a new todo.
    """
    data = todo_schema.load(request.get_json())
    todo = _create_todo(
        user_id=auth.current_user().id,
        content=data.get("content"), 
    )
    return todo_schema.dump(todo), HTTPStatus.CREATED


@todo_blueprint.get("/<int:todo_id>")
@auth.login_required
def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    query = Todo.query.filter_by(
        id=todo_id, 
        user_id=auth.current_user().id,
    )
    todo = query.first_or_404()
    return todo_schema.dump(todo)


@todo_blueprint.patch("/<int:todo_id>")
@auth.login_required
def update_todo(todo_id: int):
    """
    Update a todo by ID.
    """
    query = Todo.query.filter_by(
        id=todo_id, 
        user_id=auth.current_user().id,
    )
    todo = query.first_or_404()
    data = todo_schema.load(request.get_json())
    todo = _update_todo(
        todo=todo,
        completed=data.get("completed"),
        content=data.get("content"), 
    )
    return todo_schema.dump(todo)


@todo_blueprint.delete("/<int:todo_id>")
@auth.login_required
def delete_todo(todo_id: int):
    """
    Delete a todo by ID.
    """
    query = Todo.query.filter_by(
        id=todo_id, 
        user_id=auth.current_user().id,
    )
    todo = query.first_or_404()
    _delete_todo(todo=todo)
    return "", HTTPStatus.NO_CONTENT


@todo_blueprint.delete("")
@auth.login_required
def clear_todos():
    """
    Clears the current user's todos.
    """
    _clear_todos(user=auth.current_user())
    return "", HTTPStatus.NO_CONTENT