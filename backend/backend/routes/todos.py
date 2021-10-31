from fastapi import APIRouter


todos_router = APIRouter(prefix="/todos")


@todos_router.get("/{todo_id}")
async def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    pass


@todos_router.get("")
async def read_todos():
    """
    Get the current user's todos.
    """
    pass


@todos_router.post("")
async def create_todo():
    """
    Create a new todo.
    """
    pass


@todos_router.patch("/{todo_id}")
async def update_todo(todo_id: int):
    """
    Update a todo by ID.
    """
    pass


@todos_router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    """
    Delete a todo by ID.
    """
    pass