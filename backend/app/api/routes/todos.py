from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends

from app.api.providers import get_service, get_todo, get_current_user
from app.entities.todos import Todo
from app.entities.users import User
from app.schemas.todos import TodoSchema, TodoCreateSchema, TodoUpdateSchema
from app.services.todos import TodoService

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.get(
    path="", 
    name="todos:read-all", 
    response_model=List[TodoSchema],
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
    response_model=TodoSchema, 
)
def create_todo(
    data: TodoCreateSchema, 
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
        completed=data.completed, 
        user_id=current_user.id,
    )


@todo_router.get(
    path="/{todo_id}", 
    name="todos:read", 
    response_model=TodoSchema,
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
    response_model=TodoSchema,
)
def update_todo(
    data: TodoUpdateSchema,
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
