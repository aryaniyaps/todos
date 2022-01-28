from typing import Optional

from sqlalchemy.orm import Query


class Page(list):
    """
    Represents a paginated set of items.
    """
    pass


class PageInfo:
    """
    Contains metadata that assist in pagination.
    """
    pass


def paginate(
    query: Query, 
    cursor: Optional[int] = None, 
    limit: Optional[int] = None,
) -> Page:
    """
    description.

    :param query: The query to paginate.

    :param cursor: cursor

    :param limit: limit

    :return:
    """
    pass