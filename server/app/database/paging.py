from typing import Optional, TypeVar

from sqlalchemy.sql import Select
from sqlalchemy.orm import Mapped


T = TypeVar("T")


def paginate(
    statement: Select, 
    paginate_by: Mapped[T],
    after: Optional[T] = None, 
    per_page: Optional[int] = None,
) -> Select:
    """
    Paginates the given statement.

    :param statement: The statement to paginate.

    :param paginate_by: The attribute using which
        the given statement must be paginated.

    :param after: The attribute after which items
        must be selected.

    :param per_page: The number of items to paginate.

    :return: The paginated statement.
    """
    if after is not None:
        statement.where(paginate_by > after)
    return statement.limit(per_page)