from starlette.config import Config


config = Config()

# whether the application is in development mode.
DEBUG: bool = config("FASTAPI_DEBUG", cast=bool, default=True)

# sqlalchemy database url.
DATABASE_URL: str = config("DATABASE_URL", cast=str)

# elasticsearch configuration.
ELASTICSEARCH_URL: str = config("ELASTICSEARCH_URL", cast=str)
