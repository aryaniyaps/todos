from sqlalchemy import select, delete

from app.database.core import db_session
from app.todos.entities import Todo


class TodoRepository:
    def get_by_id(self, todo_id: int) -> Todo | None:
        """
        Get an todo with the given ID.

        :param todo_id: The todo's ID.

        :return: The todo with the given ID.
        """
        return db_session.get(Todo, todo_id)


    def get_by_user_id(self, user_id: int) -> list[Todo]:
        """
        Get todos with the given user ID.

        :param user_id: The todos' user ID.

        :return: The todos with the given user ID.
        """
        return select(Todo).filter(Todo.user_id == user_id)


    def create_todo(self, user_id: int, content: str) -> Todo:
        """
        Create a todo.

        :param user_id: The todo's user ID.

        :param content: The todo's content.

        :return: The created todo.
        """
        todo = Todo(content=content, user_id=user_id)
        db_session.add(todo)
        db_session.commit()
        return todo


    def delete_by_user_id(self, user_id: int) -> None:
        """
        Delete todos with the given user ID.

        :param user_id: The todos' user ID.
        """
        statement = delete(Todo).filter(Todo.user_id == user_id)
        db_session.execute(statement)
        db_session.commit()


    def delete_todo(self, todo: Todo) -> None:
        """
        Delete the given todo.

        :param todo: The todo to delete.
        """
        db_session.delete(todo)
        db_session.commit()


todo_repo = TodoRepository()