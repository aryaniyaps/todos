from jinja2 import Environment, PackageLoader

from app import settings


environment = Environment(
    loader=PackageLoader("app"), 
    auto_reload=settings.DEBUG
)