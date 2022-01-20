from http import HTTPStatus

from flask import Blueprint, request
from flask_login import current_user, login_required

from app.todos.schemas import (
    todo_schema, 
    todo_create_schema, 
    todo_update_schema,
    todos_schema, 
)
from app.todos.services import todo_service


todo_blueprint = Blueprint(
    name="todos", 
    import_name=__name__, 
    url_prefix="/todos",
)


@todo_blueprint.get("")
@login_required
def read_todos():
    todos = todo_service.get_todos(user=current_user)
    return todos_schema.dump(todos)


@todo_blueprint.post("")
@login_required
def create_todo():
    data = todo_create_schema.load(request.json)
    todo = todo_service.create_todo(
        user=current_user,
        content=data.content, 
    )
    return todo_schema.dump(todo), HTTPStatus.CREATED


@todo_blueprint.get("/<int:todo_id>")
@login_required
def read_todo(todo_id: int):
    todo = todo_service.get_todo(
        user=current_user,
        todo_id=todo_id, 
    )
    return todo_schema.dump(todo)


@todo_blueprint.patch("/<int:todo_id>")
@login_required
def update_todo(todo_id: int):
    data = todo_update_schema.load(request.json)
    todo = todo_service.update_todo(
        user=current_user,
        todo_id=todo_id, 
        completed=data.completed, 
        content=data.content,
    )
    return todo_schema.dump(todo)


@todo_blueprint.delete("/<int:todo_id>")
@login_required
def delete_todo(todo_id: int):
    todo_service.delete_todo(
        user=current_user, 
        todo_id=todo_id,
    )
    return "", HTTPStatus.NO_CONTENT


@todo_blueprint.delete("")
@login_required
def clear_todos():
    todo_service.clear_todos(user=current_user)
    return "", HTTPStatus.NO_CONTENT
