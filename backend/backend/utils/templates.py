from jinja2 import Environment, PackageLoader, select_autoescape

__all__ = ("render_template",)

environment = Environment(
    loader=PackageLoader("backend"),
    autoescape=select_autoescape(),
)


def render_template(template_name: str, **kwargs):
    """
    Renders the template found with the given variables.

    :param template_name: The name of the template to find.
    """
    template = environment.get_template(name=template_name)
    return template.render(**kwargs)