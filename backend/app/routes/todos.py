from http import HTTPStatus

from sanic import Blueprint, Request
from sanic.response import empty, json
from flask_login import login_required, current_user

from app.core.database import get_session
from app.models.todos import Todo
from app.schemas.todos import todo_schema, todos_schema


todo_blueprint = Blueprint("todos", url_prefix="/todos")


@todo_blueprint.get("")
@login_required
def read_todos(request: Request):
    """
    Get the current user's todos.
    """
    query = Todo.query.filter_by(user_id=current_user.id)
    page = request.args.get(key="page", default=1, type=int)
    limit = request.args.get(key="limit", default=20, type=int)
    results = query.paginate(page, limit, False)
    return json({
        "has_prev": results.has_prev,
        "has_next": results.has_next,
        "total": results.total,
        "results": todos_schema.dump(results.items)
    })


@todo_blueprint.post("")
@login_required
def create_todo(request: Request):
    """
    Create a new todo.
    """
    data = todo_schema.load(request.get_json())
    todo = Todo(
        content=data.get("content"), 
        user_id=current_user.id
    )
    with get_session() as session:
        session.add(todo)
        session.commit()
    return json(
        todo_schema.dump(todo), 
        status=HTTPStatus.CREATED
    )


@todo_blueprint.get("/<todo_id:int>")
@login_required
def read_todo(request: Request, todo_id: int):
    """
    Get a todo by ID.
    """
    query = Todo.query.filter_by(
        id=todo_id, 
        user_id=current_user.id,
    )
    todo = query.first_or_404()
    return json(todo_schema.dump(todo))


@todo_blueprint.patch("/<todo_id:int>")
@login_required
def update_todo(request: Request, todo_id: int):
    """
    Update a todo by ID.
    """
    query = Todo.query.filter_by(
        id=todo_id, 
        user_id=current_user.id,
    )
    todo = query.first_or_404()
    data = todo_schema.load(request.get_json())
    content = data.get("content")
    completed = data.get("completed")
    if content is not None:
        todo.content = content
    if completed is not None:
        todo.completed = completed
    with get_session() as session:
        session.add(todo)
        session.commit()
    return json(todo_schema.dump(todo))


@todo_blueprint.delete("/<todo_id:int>")
@login_required
def delete_todo(request: Request, todo_id: int):
    """
    Delete a todo by ID.
    """
    query = Todo.query.filter_by(
        id=todo_id, 
        user_id=current_user.id,
    )
    todo = query.first_or_404()
    with get_session() as session:
        session.delete(todo)
        session.commit()
    return empty()


@todo_blueprint.delete("")
@login_required
def clear_todos(request: Request):
    """
    Clears the current user's todos.
    """
    Todo.query.filter_by(user_id=current_user.id).delete()
    return empty()