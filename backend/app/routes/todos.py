from http import HTTPStatus

from flask import Blueprint, request

from app.core.auth import auth
from app.extensions import db
from app.models.todos import Todo
from app.schemas.todos import todo_schema, todos_schema


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
    content = data.get("content")
    user_id = auth.current_user().id
    todo = Todo(content=content, user_id=user_id)
    db.session.add(todo)
    db.session.commit()
    db.session.refresh(todo)
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
    content = data.get("content")
    completed = data.get("completed")
    if content is not None:
        todo.content = content
    if completed is not None:
        todo.completed = completed
    db.session.commit()
    db.session.refresh(todo)
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
    db.session.delete(todo)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT


@todo_blueprint.delete("")
@auth.login_required
def clear_todos():
    """
    Clears the current user's todos.
    """
    user = auth.current_user()
    Todo.query.filter_by(user_id=user.id).delete()
    return "", HTTPStatus.NO_CONTENT