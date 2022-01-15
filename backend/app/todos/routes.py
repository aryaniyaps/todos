from http import HTTPStatus
from typing import List

from flask import Blueprint

from app.todos.entities import Todo
from app.users.entities import User
from app.todos.services import todo_service


todo_blueprint = Blueprint("todos", __name__, url_prefix="/todos")


@todo_blueprint.get("")
def read_todos(
    current_user: User = Depends(
        dependency=get_current_user
    ),
) -> List[Todo]:
    """
    Get the current user's todos.
    """
    return todo_service.get_todos(user_id=current_user.id)


@todo_blueprint.post("")
def create_todo(
    data: TodoCreateInput, 
    current_user: User = Depends(
        dependency=get_current_user
    ), 
) -> Todo:
    """
    Create a new todo.
    """
    return todo_service.create_todo(
        content=data.content,  
        user_id=current_user.id,
    )


@todo_blueprint.get("/<todo_id:int>")
def read_todo(
    todo: Todo = Depends(
        dependency=get_todo,
    ),
) -> Todo:
    """
    Get a todo by ID.
    """
    return todo


@todo_blueprint.patch("/<todo_id:int>")
def update_todo(
    data: TodoUpdateInput,
    todo: Todo = Depends(
        dependency=get_todo,
    ),
) -> Todo:
    """
    Update a todo by ID.
    """
    return todo_service.update_todo(
        todo=todo, 
        completed=data.completed, 
        content=data.content,
    )


@todo_blueprint.delete("/<todo_id:int>")
def delete_todo(
    todo: Todo = Depends(
        dependency=get_todo,
    ), 
) -> None:
    """
    Delete a todo by ID.
    """
    todo_service.delete_todo(todo=todo)


@todo_blueprint.delete("")
def clear_todos(
    current_user: User = Depends(
        dependency=get_current_user
    ), 
) -> None:
    """
    Clear the current user's todos.
    """
    todo_service.clear_todos(user_id=current_user.id)
    return "", HTTPStatus.NO_CONTENT
