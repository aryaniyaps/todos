from app.database.core import db_session
from app.database.paging import paginate
from app.users.entities import User


def test_paginate() -> None:
    """
    Ensure we can paginate a select statement.
    """
    pass


def test_paginate_by() -> None:
    """
    Ensure we can paginate by a specific 
    paging attribute.
    """
    pass


def test_paginate_after() -> None:
    """
    Ensure we can paginate a statement
    after the given paging attribute value.
    """
    pass


def test_paginate_per_page() -> None:
    """
    Ensure we can paginate a statement
    with the correct number of items per page.
    """
    pass