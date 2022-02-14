from app.todos.entities import Todo
from app.todos.repositories import TodoRepo
from app.users.entities import User


def test_get_todos(user: User) -> None:
    """
    Ensure we can get todos for a given user.
    """
    results = TodoRepo.get_todos(user_id=user.id)
    assert results


def test_get_todo(todo: Todo) -> None:
    """
    Ensure we can get a todo.
    """
    result = TodoRepo.get_todo(
        todo_id=todo.id, 
        user_id=todo.user_id,
    )
    assert result == todo
        

def test_create_todo(user: User) -> None:
    """
    Ensure we can create a todo.
    """
    content = "content"
    result = TodoRepo.create_todo(
        content=content,
        user_id=user.id,
    )
    assert result.content == content
    assert result.user_id == user.id
    assert not result.completed


def test_update_todo(todo: Todo) -> None:
    """
    Ensure we can update a todo.
    """
    content = "content"
    result = TodoRepo.update_todo(
        todo=todo, 
        completed=True, 
        content=content,
    )
    assert result.content == content
    assert result.completed


def test_delete_todo(todo: Todo) -> None:
    """
    Ensure we can delete a todo.
    """
    TodoRepo.delete_todo(todo=todo)
    result = TodoRepo.get_todo(
        user_id=todo.user_id,
        todo_id=todo.id,
    )
    assert result is None


def test_clear_todos(user: User) -> None:
    """
    Ensure we can clear todos for a user.
    """
    TodoRepo.clear_todos(user_id=user.id)
    assert not user.todos
