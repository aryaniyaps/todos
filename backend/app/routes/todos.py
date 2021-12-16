from http import HTTPStatus

from sanic import Blueprint, Request
from sanic.exceptions import NotFound
from sanic.response import empty, json

from app.core.auth import login_required
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
    offset = request.args.get(key="offset", default=1, type=int)
    limit = request.args.get(key="limit", default=20, type=int)
    with get_session() as session:
        todos = session.query(Todo).filter_by(user_id=current_user.id)
        todos.offset(offset).limit(limit)
    return json(todos_schema.dump(todos))


@todo_blueprint.post("")
@login_required
def create_todo(request: Request):
    """
    Create a new todo.
    """
    data = todo_schema.load(request.json)
    with get_session() as session:
        todo = Todo(
            content=data.get("content"), 
            user_id=current_user.id
        )
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
    with get_session() as session:
        todo = session.query(Todo).filter_by(
            id=todo_id, 
            user_id=current_user.id
        )
    if todo is None:
        raise NotFound("Couldn't find the requested todo.")
    return json(todo_schema.dump(todo))


@todo_blueprint.patch("/<todo_id:int>")
@login_required
def update_todo(request: Request, todo_id: int):
    """
    Update a todo by ID.
    """
    with get_session() as session:
        todo = session.query(Todo).filter_by(
            id=todo_id, 
            user_id=current_user.id
        )
        if todo is None:
            raise NotFound("Couldn't find the requested todo.")
        data = todo_schema.load(request.json)
        content = data.get("content")
        completed = data.get("completed")
        if content is not None:
            todo.content = content
        if completed is not None:
            todo.completed = completed
        session.add(todo)
        session.commit()
    return json(todo_schema.dump(todo))


@todo_blueprint.delete("/<todo_id:int>")
@login_required
def delete_todo(request: Request, todo_id: int):
    """
    Delete a todo by ID.
    """
    with get_session() as session:
        todo = session.query(Todo).filter_by(
            id=todo_id, 
            user_id=current_user.id
        )
        if todo is None:
            raise NotFound("Couldn't find the requested todo.")
        session.delete(todo)
        session.commit()
    return empty()


@todo_blueprint.delete("")
@login_required
def clear_todos(request: Request):
    """
    Clears the current user's todos.
    """
    with get_session() as session:
        todos = session.query(Todo).filter_by(
            user_id=current_user.id
        )
        todos.delete()
    return empty()