from sanic import Request
from sanic.response import HTTPResponse


def security_middleware(request: Request, response: HTTPResponse) -> None:
    """Sets security headers on the response."""
    response.headers.setdefault("X-Frame-Options", "deny")
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-XSS-Protection", "1; mode=block")