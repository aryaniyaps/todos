from inspect import isawaitable
from functools import wraps, partial

from fastapi import Request
from fastapi.exceptions import Unauthorized


def check_auth(request: Request) -> bool:
    """
    Checks whether the given request is authenticated.

    :param request: The HTTP request to check.

    :return: Whether the request is authenticated.
    """
    pass


def login_required(route):
    """
    Decorator to secure the given route behind a login.

    :param route: The route to be protected.
    """
    if route is None:
        return partial(login_required)
    
    @wraps(route)
    async def protected_route(request: Request, *args, **kwargs):
        if not check_auth(request=request):
            raise Unauthorized(message="Could not find credentials.")
        response = route(request, *args, **kwargs)
        if isawaitable(response):
            response = await response
        return response

    return protected_route