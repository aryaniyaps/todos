from jinja2 import Environment, PackageLoader

from app.config import DEBUG, PUBLIC_SITE_NAME


environment = Environment(
    loader=PackageLoader("app"), 
    auto_reload=DEBUG
)

environment.make_globals({
    "site_name": PUBLIC_SITE_NAME
})