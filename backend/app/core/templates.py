from jinja2 import Environment, PackageLoader

from app.config import DEBUG


environment = Environment(
    loader=PackageLoader("app"), 
    auto_reload=DEBUG
)