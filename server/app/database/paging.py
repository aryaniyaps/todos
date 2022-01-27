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
    after: Optional[int] = None, 
    before: Optional[int] = None,
    limit: Optional[int] = None, 
    reversed = False,
) -> Page:
    """
    description.

    :param after: after

    :param before: before

    :param limit: limit

    :param reversed: reversed

    :return:
    """
    pass