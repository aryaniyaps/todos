from typing import List, Optional

from sqlalchemy import select, delete

from app.core.database import db_session
from app.todos.entities import Todo


class TodoService:
    def get_todos(self, *, user_id: int) -> List[Todo]:
        """
        Gets todos with the given user ID.

        :param user_id: The todos' owner ID.

        :return: The user's todos.
        """
        statement = select(Todo).filter_by(user_id=user_id)
        return db_session.execute(statement).scalars()

    def get_todo(self, *, todo_id: int, user_id: int) -> Optional[Todo]:
        """
        Gets a todo with the given ID.

        :param todo_id: The todo's ID.

        :param user_id: The todo's owner ID.

        :return: The user's todo.
        """
        statement = select(Todo).filter_by(id=todo_id, user_id=user_id)
        return db_session.scalars(statement).first()

    def create_todo(
        self, *, 
        content: str, 
        user_id: int, 
    ) -> Todo:
        """
        Creates a todo with the given data.

        :param content: The todo's content.

        :param user_id: The todos's owner ID.

        :return: The created todo.
        """
        todo = Todo(
            content=content, 
            user_id=user_id,
        )
        db_session.add(todo)
        db_session.commit()
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
        db_session.add(todo)
        db_session.commit()
        return todo

    def delete_todo(self, *, todo: Todo) -> None:
        """
        Deletes the given todo.

        :param todo: The todo to delete.
        """
        db_session.delete(todo)
        db_session.commit()

    def clear_todos(self, *, user_id: int) -> None:
        """
        Deletes todos owned by the user with the given ID.

        :param user_id: The owner ID of the todos.
        """
        statement = delete(Todo).filter_by(user_id=user_id)
        db_session.execute(statement)
