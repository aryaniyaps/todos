from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user

from backend.models.todos import Todo
from backend.services.todos import create_todo, delete_todo
from backend.schemas.todos import TodoSchema


todo_blueprint = Blueprint("todos", __name__, url_prefix="/todos")


@todo_blueprint.get("/<int:todo_id>")
@login_required
def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    query = Todo.query.filter_by(id=todo_id, user_id=current_user.id)
    todo = query.first_or_404()
    data = TodoSchema().dump(todo)
    return jsonify({"todo": data}), HTTPStatus.OK


@todo_blueprint.get("")
@login_required
def read_todos():
    """
    Get the current user's todos.
    """
    todos = Todo.query.filter_by(user_id=current_user.id)
    data = TodoSchema(many=True).dump(todos)
    return jsonify({"todos": data}), HTTPStatus.OK


@todo_blueprint.post("")
@login_required
def create_todo():
    """
    Create a new todo.
    """
    data = request.get_json()
    schema = TodoSchema()
    validated_data, errors = schema.load(data)
    if errors:
        return jsonify(errors), HTTPStatus.BAD_REQUEST
    create_todo(
        user_id=current_user.id,
        content=validated_data.get("content"), 
    )
    return jsonify(schema.dump(schema.instance).data), HTTPStatus.CREATED


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
    query = Todo.query.filter_by(id=todo_id, user_id=current_user.id)
    todo = query.first_or_404()
    delete_todo(todo=todo)
    return "", HTTPStatus.NO_CONTENT