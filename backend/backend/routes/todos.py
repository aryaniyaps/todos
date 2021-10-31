from fastapi import APIRouter


todo_router = APIRouter(prefix="/todos")


@todo_router.get("/{todo_id}", name="todos:read")
async def read_todo(todo_id: int):
    """
    Get a todo by ID.
    """
    pass


@todo_router.get("", name="todos:read-all")
async def read_todos():
    """
    Get the current user's todos.
    """
    pass


@todo_router.post("", name="todos:create")
async def create_todo():
    """
    Create a new todo.
    """
    pass


@todo_router.patch("/{todo_id}", name="todos:update")
async def update_todo(todo_id: int):
    """
    Update a todo by ID.
    """
    pass


@todo_router.delete("/{todo_id}", name="todos:delete")
async def delete_todo(todo_id: int):
    """
    Delete a todo by ID.
    """
    pass