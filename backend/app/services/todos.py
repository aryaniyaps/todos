from typing import List, Optional

from app.entities.todos import Todo
from app.services.base import BaseService


class TodoService(BaseService):
    def get_todos(self, *, user_id: int) -> List[Todo]:
        """
        Gets todos with the given user ID.

        :param user_id: The todos' owner ID.

        :return: The user's todos.
        """
        return self.session.query(Todo).filter_by(user_id=user_id)

    def get_todo(self, *, todo_id: int, user_id: int) -> Optional[Todo]:
        """
        Gets a todo with the given ID.

        :param todo_id: The todo's ID.

        :param user_id: The todo's owner ID.

        :return: The user's todo.
        """
        query = self.session.query(Todo)
        query.filter_by(id=todo_id, user_id=user_id)
        return query.first()

    def create_todo(
        self, *, 
        content: str, 
        user_id: int, 
        completed: bool = False,
    ) -> Todo:
        """
        Creates a todo with the given data.

        :param content: The todo's content.

        :param user_id: The todos's owner ID.

        :param completed: Whether the todo is completed.

        :return: The created todo.
        """
        todo = Todo(
            content=content, 
            user_id=user_id, 
            completed=completed,
        )
        self.session.add(todo)
        self.session.commit()
        return todo

    def update_todo(
        self,
        *,
        todo: Todo,
        completed: Optional[bool] = None,
        content: Optional[str] = None,
    ) -> Todo:
        """
        Updates a todo with the given data.

        :param todo: The todo to update.

        :param completed: Whether the todo is completed.

        :param content: The todo's content.

        :return: The updated todo.
        """
        if content is not None:
            todo.content = content
        if completed is not None:
            todo.completed = completed
        self.session.add(todo)
        self.session.commit()
        return todo

    def delete_todo(self, *, todo: Todo) -> None:
        """
        Deletes the given todo.

        :param todo: The todo to delete.
        """
        self.session.delete(todo)
        self.session.commit()

    def clear_todos(self, *, user_id: int) -> None:
        """
        Deletes todos owned by the user with the given ID.

        :param user_id: The owner ID of the todos.
        """
        todos = self.session.query(Todo)
        todos.filter_by(user_id=user_id)
        todos.delete()
