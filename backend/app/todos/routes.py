from typing import List

from flask import Blueprint

from app.api.providers import get_service, get_todo, get_current_user
from app.todos.entities import Todo
from app.users.entities import User
from app.todos.models import TodoCreateInput, TodoUpdateInput
from app.todos.services import TodoService

todo_blueprint = Blueprint(url_prefix="/todos")


@todo_blueprint.get("")
def read_todos(
    current_user: User = Depends(
        dependency=get_current_user
    ), 
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
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
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
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
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
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
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
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
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
) -> None:
    """
    Clear the current user's todos.
    """
    todo_service.clear_todos(user_id=current_user.id)
