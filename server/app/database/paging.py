from typing import TypeVar

from sqlalchemy.engine import ScalarResult
from sqlalchemy.sql import Select
from sqlalchemy.orm import Mapped

from app.database.core import db_session


T = TypeVar("T")


def paginate(
    statement: Select, 
    paginate_by: Mapped[T],
    after: T | None = None, 
    per_page: int | None = None,
) -> ScalarResult:
    """
    Paginate the given statement.

    :param statement: The statement to paginate.

    :param paginate_by: The attribute using which
        the given statement must be paginated.

    :param after: The attribute value after which 
        entities must be selected.

    :param per_page: The number of entities to show 
        in a page.

    :return: The paginated statement.
    """
    if after is not None:
        statement.filter(paginate_by > after)
    statement.limit(per_page)
    # TODO: return a page object with additional
    # paging metadata here.
    return db_session.scalars(statement)