from app.todos.entities import Todo
from app.todos.repositories import todo_repo
from app.users.entities import User


def test_get_todos(user: User) -> None:
    """
    Ensure we can get todos for a given user.
    """
    results = todo_repo.get_todos(user_id=user.id)
    assert results


def test_get_todo(todo: Todo) -> None:
    """
    Ensure we can get a todo.
    """
    result = todo_repo.get_todo(
        todo_id=todo.id, 
        user_id=todo.user_id,
    )
    assert result == todo
        

def test_create_todo(user: User) -> None:
    """
    Ensure we can create a todo.
    """
    content = "content"
    result = todo_repo.create_todo(
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
    result = todo_repo.update_todo(
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
    todo_repo.delete_todo(todo=todo)
    result = todo_repo.get_todo(
        user_id=todo.user_id,
        todo_id=todo.id,
    )
    assert result is None


def test_clear_todos(user: User) -> None:
    """
    Ensure we can clear todos for a user.
    """
    todo_repo.clear_todos(user_id=user.id)
    assert not user.todos
