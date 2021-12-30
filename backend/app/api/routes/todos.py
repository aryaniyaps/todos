from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.api.dependencies import get_service, get_todo, get_current_user
from app.models.todos import Todo
from app.models.users import User
from app.schemas.todos import TodoCreate, TodoUpdate
from app.services.todos import TodoService

todo_router = APIRouter(prefix="/todos")


@todo_router.get("", name="todos:read-all")
def read_todos(
    current_user: User = Depends(
        dependency=get_current_user
    ), 
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
):
    """
    Get the current user's todos.
    """
    return todo_service.get_todos(user_id=current_user.id)


@todo_router.post("", name="todos:create", status_code=HTTPStatus.CREATED)
def create_todo(
    data: TodoCreate, 
    current_user: User = Depends(
        dependency=get_current_user
    ), 
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
):
    """
    Create a new todo.
    """
    return todo_service.create_todo(
        content=data.content, 
        completed=data.completed, 
        user_id=current_user.id,
    )


@todo_router.get("/{todo_id}", name="todos:read")
def read_todo(todo: Todo = Depends(dependency=get_todo)):
    """
    Get a todo by ID.
    """
    return todo


@todo_router.patch("/{todo_id}", name="todos:update")
def update_todo(
    data: TodoUpdate,
    todo: Todo = Depends(dependency=get_todo),
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
):
    """
    Update a todo by ID.
    """
    return todo_service.update_todo(
        todo=todo, completed=data.completed, content=data.content
    )


@todo_router.delete(
    "/{todo_id}", 
    name="todos:delete", 
    status_code=HTTPStatus.NO_CONTENT,
)
def delete_todo(
    todo: Todo = Depends(dependency=get_todo), 
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
):
    """
    Delete a todo by ID.
    """
    todo_service.delete_todo(todo=todo)


@todo_router.delete("", name="todos:clear", status_code=HTTPStatus.NO_CONTENT)
def clear_todos(
    current_user: User = Depends(
        dependency=get_current_user
    ), 
    todo_service: TodoService = Depends(
        dependency=get_service(
            service=TodoService,
        ),
    ),
):
    """
    Clears the current user's todos.
    """
    todo_service.clear_todos(user_id=current_user.id)
