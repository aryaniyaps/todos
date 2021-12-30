from jinja2 import Environment, PackageLoader

from app.config import settings

environment = Environment(loader=PackageLoader("app"), auto_reload=settings.DEBUG)

environment.make_globals({"site_name": settings.SITE_NAME})
