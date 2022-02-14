from app.errors import ResourceNotFound
from app.todos.entities import Todo
from app.todos.repositories import TodoRepo


class TodoService:
    @classmethod
    def get_todos(
        cls, 
        user_id: int, 
        per_page: int | None = None,
        after: int | None = None, 
    ) -> list[Todo]:
        """
        Get the given user's todos.

        :param user_id: The todos' owner ID.

        :param after: The todo ID after which 
            todos must be selected.

        :param per_page: The number of todos to 
            show per page.

        :return: The user's todos.
        """
        return TodoRepo.get_todos(
            user_id=user_id, 
            per_page=per_page, 
            after=after,
        )


    @classmethod
    def get_todo(cls, user_id: int, todo_id: int) -> Todo:
        """
        Get a todo with the given ID.

        :param user_id: The todo's owner ID.

        :param todo_id: The todo's ID.

        :return: The user's todo.
        """
        todo = TodoRepo.get_todo(
            todo_id=todo_id, 
            user_id=user_id,
        )
        if todo is None:
            raise ResourceNotFound(
                message=f"Could not find todo with ID {todo_id}.",
            )
        return todo


    @classmethod
    def create_todo(cls, user_id: int, content: str) -> Todo:
        """
        Create a todo.

        :param user_id: The todo's owner ID.

        :param content: The todo's content.

        :return: The created todo.
        """
        return TodoRepo.create_todo(
            user_id=user_id, 
            content=content,
        )


    @classmethod
    def update_todo(
        cls,
        user_id: int,
        todo_id: int,
        completed: bool | None = None,
        content: str | None = None,
    ) -> Todo:
        """
        Update the todo with the given ID.

        :param user_id: The todo's owner ID.

        :param todo_id: ID of the todo to update.

        :param completed: Whether the todo is completed.

        :param content: The todo's content.

        :return: The updated todo.
        """
        return TodoRepo.update_todo(
            todo=cls.get_todo(
                user_id=user_id, 
                todo_id=todo_id,
            ),
            completed=completed,
            content=content,
        )


    @classmethod
    def delete_todo(cls, user_id: int, todo_id: int) -> None:
        """
        Delete the todo with the given ID.

        :param user_id: The todo's owner ID.

        :param todo_id: ID of the todo to delete.
        """
        TodoRepo.delete_todo(
            todo=cls.get_todo(
                user_id=user_id,
                todo_id=todo_id,
            ),
        )


    @classmethod
    def clear_todos(cls, user_id: int) -> None:
        """
        Clear the given user's todos.

        :param user_id: The todos' user ID.
        """
        TodoRepo.clear_todos(user_id=user_id)