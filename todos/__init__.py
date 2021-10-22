from flask import Flask

from todos.extensions import cors, cache, db, migrate


__all__ = ("application",)


def create_app(config: str = "todos.settings") -> Flask:
    """
    Initializes an app instance.

    :param config: The configuration file to use.
    :return: The created app.
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app: Flask) -> None:
    """
    Registers extensions for the given app.

    :param app: The app the register extensions for.
    """
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    cors.init_app(app)


def register_blueprints(app: Flask) -> None:
    """
    Registers blueprints for the given app.

    :param app: The app the register blueprints for.
    """
    pass


application = create_app()
