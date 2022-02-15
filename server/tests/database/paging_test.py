from app.database.core import db_session
from app.database.paging import paginate
from app.users.entities import User


def test_paginate(user: User) -> None:
    """
    Ensure we can paginate a select statement.
    """
    pass


def test_paginate_by(user: User) -> None:
    """
    Ensure we can paginate by the given 
    paging attribute.
    """
    pass


def test_paginate_after(user: User) -> None:
    """
    Ensure we can paginate a statement
    after the given paging attribute value.
    """
    pass


def test_paginate_per_page(user: User) -> None:
    """
    Ensure we can paginate a statement
    with the given page limit.
    """
    pass
