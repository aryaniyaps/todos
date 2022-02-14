from sqlalchemy import select, delete

from app.database.core import db_session
from app.database.paging import paginate
from app.todos.entities import Todo


class TodoRepo:
    @classmethod
    def get_todo(cls, todo_id: int, user_id: int) -> Todo | None:
        """
        Get an todo with the given ID.

        :param todo_id: The todo's ID.

        :param user_id: The todo's user ID.

        :return: The todo with the given ID.
        """
        return db_session.get(Todo, (todo_id, user_id))


    @classmethod
    def get_todos(
        cls, 
        user_id: int, 
        after: int | None = None, 
        per_page: int | None = None,
    ) -> list[Todo]:
        """
        Get todos with the given user ID.

        :param user_id: The todos' user ID.

        :param after: The todo ID after which 
            todos must be selected.

        :param per_page: The number of todos to 
            show per page.

        :return: The todos with the given user ID.
        """
        statement = select(Todo).filter(Todo.user_id == user_id)
        return db_session.scalars(
            paginate(
                statement=statement, 
                paginate_by=Todo.id, 
                after=after, 
                per_page=per_page,
            )
        )


    @classmethod
    def create_todo(cls, user_id: int, content: str) -> Todo:
        """
        Create a todo.

        :param user_id: The todo's user ID.

        :param content: The todo's content.

        :return: The created todo.
        """
        todo = Todo(
            content=content, 
            user_id=user_id,
        )
        db_session.add(todo)
        db_session.commit()
        return todo


    @classmethod
    def update_todo(
        cls,
        todo: Todo,
        completed: bool | None = None,
        content: str | None = None,
    ) -> Todo:
        """
        Update the given todo.

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


    @classmethod
    def clear_todos(cls, user_id: int) -> None:
        """
        Clear todos with the given user ID.

        :param user_id: The todos' user ID.
        """
        db_session.execute(
            delete(Todo).filter(
                Todo.user_id == user_id,
            ),
        )
        db_session.commit()


    @classmethod
    def delete_todo(cls, todo: Todo) -> None:
        """
        Delete the given todo.

        :param todo: The todo to delete.
        """
        db_session.delete(todo)
        db_session.commit()
