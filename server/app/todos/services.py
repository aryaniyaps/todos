from app.errors import ResourceNotFound
from app.todos.entities import Todo
from app.todos.repositories import todo_repo
from app.users.entities import User


class TodoService:
    def get_todos(
        self, 
        user: User, 
        per_page: int | None = None,
        after: int | None = None, 
    ) -> list[Todo]:
        """
        Get the given user's todos.

        :param user: The todos' owner.

        :param after: The todo ID after which 
            todos must be selected.

        :param per_page: The number of todos to 
            show per page.

        :return: The user's todos.
        """
        return todo_repo.get_todos(
            user_id=user.id, 
            per_page=per_page, 
            after=after,
        )

    def get_todo(self, user: User, todo_id: int) -> Todo:
        """
        Get a todo with the given ID.

        :param user: The todo's owner.

        :param todo_id: The todo's ID.

        :return: The user's todo.
        """
        todo = todo_repo.get_todo(todo_id=todo_id, user_id=user.id)
        if todo is None:
            raise ResourceNotFound(
                message=f"Could not find todo with ID {todo_id}.",
            )
        return todo

    def create_todo(self, user: User, content: str) -> Todo:
        """
        Create a todo.

        :param user: The todo's owner.

        :param content: The todo's content.

        :return: The created todo.
        """
        return todo_repo.create_todo(
            user_id=user.id, 
            content=content,
        )

    def update_todo(
        self,
        user: User,
        todo_id: int,
        completed: bool | None = None,
        content: str | None = None,
    ) -> Todo:
        """
        Update the todo with the given ID.

        :param user: The todo's owner.

        :param todo_id: ID of the todo to update.

        :param completed: Whether the todo is completed.

        :param content: The todo's content.

        :return: The updated todo.
        """
        return todo_repo.update_todo(
            todo=self.get_todo(
                user=user, 
                todo_id=todo_id,
            ),
            completed=completed,
            content=content
        )

    def delete_todo(self, user: User, todo_id: int) -> None:
        """
        Delete the todo with the given ID.

        :param user: The todo's owner.

        :param todo_id: ID of the todo to delete.
        """
        todo_repo.delete_todo(
            todo=self.get_todo(
                user=user,
                todo_id=todo_id
            )
        )

    def clear_todos(self, user: User) -> None:
        """
        Clear the given user's todos.

        :param user: The todos' user.
        """
        todo_repo.clear_todos(user_id=user.id)


todo_service = TodoService()