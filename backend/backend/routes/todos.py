from http import HTTPStatus

from flask import Blueprint, request
from flask_login import login_required, current_user

from backend.models.todos import Todo
from backend.services.todos import create_todo, delete_todo, update_todo
from backend.schemas.todos import TodoSchema


todo_blueprint = Blueprint(
    name="todos", 
    import_name=__name__, 
    url_prefix="/todos",
)


@todo_blueprint.get("/<int:todo_id>")
@login_required
def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    query = Todo.query.filter(
        Todo.id == todo_id, 
        Todo.user_id == current_user.id,
    )
    todo = query.first_or_404()
    data = TodoSchema().dump(todo)
    return {"todo": data}


@todo_blueprint.get("")
@login_required
def read_todos():
    """
    Get the current user's todos.
    """
    query = Todo.query.filter(
        Todo.user_id == current_user.id,
    )
    page = request.args.get(key="page", default=1, type=int)
    limit = request.args.get(key="limit", default=20, type=int)
    result = query.paginate(page=page, per_page=limit, error_out=False)
    todos = TodoSchema(many=True).dump(result.items)
    return {
        "todos": todos,
        "has_prev": result.has_prev,
        "has_next": result.has_next,
        "count": result.total
    }


@todo_blueprint.post("")
@login_required
def create_todo():
    """
    Create a new todo.
    """
    schema = TodoSchema()
    data = schema.load(request.get_json())
    todo = create_todo(
        user_id=current_user.id,
        content=data.get("content"), 
    )
    return {"todo": schema.dump(todo)}


@todo_blueprint.patch("/<int:todo_id>")
@login_required
def update_todo(todo_id: int):
    """
    Update a todo by ID.
    """
    query = Todo.query.filter(
        Todo.id == todo_id, 
        Todo.user_id == current_user.id,
    )
    todo = query.first_or_404()
    schema = TodoSchema()
    data = schema.load(request.get_json())
    todo = update_todo(
        todo=todo,
        completed=data.get("completed"),
        content=data.get("content"), 
    )
    return {"todo": schema.dump(todo)}


@todo_blueprint.delete("/<int:todo_id>")
@login_required
def delete_todo(todo_id: int):
    """
    Delete a todo by ID.
    """
    query = Todo.query.filter(
        Todo.id == todo_id, 
        Todo.user_id == current_user.id,
    )
    todo = query.first_or_404()
    delete_todo(todo=todo)
    return "", HTTPStatus.NO_CONTENT