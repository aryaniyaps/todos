from dataclasses import dataclass
from typing import Generic, TypeVar

from sqlalchemy.orm import Mapped
from sqlalchemy.sql import Select

from app.database.core import db_session


CT = TypeVar("CT")

ET = TypeVar("ET")


@dataclass
class PageMeta(Generic[CT]):
    """
    Represents additional metadata 
    that aids in pagination.

    :param has_prev: When paginating backwards, 
        are there more items?

    :param has_next: When paginating forwards, 
        are there more items?

    :param start_cursor: When paginating backwards, 
        the cursor to continue.

    :param end_cursor: When paginating forwards, 
        the cursor to continue.
    """
    has_prev: bool
    has_next: bool
    start_cursor: CT
    end_cursor: CT


@dataclass
class Page(Generic[ET]):
    """
    Represents a paginated sequence of entities.

    :param entities: A sequence of entities in the Page.

    :param page_meta: Metadata to aid in pagination.
    """
    entities: list[ET]
    page_meta: PageMeta


def paginate(
    statement: Select, 
    paginate_by: Mapped[CT],
    after: CT | None = None, 
    per_page: int | None = None,
) -> Page:
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
    entities = db_session.scalars(statement)
    return Page(
        entities=entities,
        page_meta=PageMeta(
            has_next=True,
            has_prev=False,
            end_cursor="",
            start_cursor=""
        )
    )