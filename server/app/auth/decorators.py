from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from flask import session

from app.errors import Unauthenticated


RT = TypeVar("RT")

P = ParamSpec("P")


def auth_required(route: Callable[P, RT]) -> Callable[P, RT]:
    @wraps(route)
    def protected_route(*args: P.args, **kwargs: P.kwargs) -> RT:
        if session.get("user_id") is None:
            raise Unauthenticated(
                message="Could not validate credentials.",
            )
        return route(*args, **kwargs)
    return protected_route