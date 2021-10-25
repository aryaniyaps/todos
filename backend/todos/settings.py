from starlette.config import Config


config = Config(env_file=".env")

# whether the application is in development mode.
DEBUG: bool = config("FASTAPI_DEBUG", cast=bool, default=True)

# sqlalchemy database url.
DATABASE_URL: str = config("DATABASE_URL", cast=str)

# elasticsearch configuration.
ELASTIC_SEARCH_URL: str = config("ELASTIC_SEARCH_URL", cast=str)
