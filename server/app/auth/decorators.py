from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from flask import session

from app.errors import Unauthenticated


R = TypeVar("R")

P = ParamSpec("P")


def auth_required(route: Callable[P, R]) -> Callable[P, R]:
    """
    Protect the given route with an authentication
    check. Wrapping the route with this decorator ensures
    that the current user will be authenticated before
    the route call.

    :param route: The route to protect.

    :return: The protected route.
    """
    @wraps(wrapped=route)
    def protected_route(*args: P.args, **kwargs: P.kwargs) -> R:
        if session.get("user_id") is None:
            raise Unauthenticated(
                message="Could not validate credentials.",
            )
        return route(*args, **kwargs)
    return protected_route