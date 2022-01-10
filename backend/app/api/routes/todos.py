from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends

from app.api.providers import get_service, get_todo, get_current_user
from app.entities.todos import Todo
from app.entities.users import User
from app.models.todos import TodoModel, TodoCreateInput, TodoUpdateInput
from app.services.todos import TodoService

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.get(
    path="", 
    name="todos:read-all", 
    response_model=List[TodoModel],
)
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


@todo_router.post(
    path="",
    name="todos:create", 
    status_code=HTTPStatus.CREATED,
    response_model=TodoModel, 
)
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


@todo_router.get(
    path="/{todo_id}", 
    name="todos:read", 
    response_model=TodoModel,
)
def read_todo(
    todo: Todo = Depends(
        dependency=get_todo,
    ),
) -> Todo:
    """
    Get a todo by ID.
    """
    return todo


@todo_router.patch(
    path="/{todo_id}", 
    name="todos:update", 
    response_model=TodoModel,
)
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


@todo_router.delete(
    path="/{todo_id}", 
    name="todos:delete",
    status_code=HTTPStatus.NO_CONTENT,
)
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


@todo_router.delete(
    path="", 
    name="todos:clear", 
    status_code=HTTPStatus.NO_CONTENT,
)
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
