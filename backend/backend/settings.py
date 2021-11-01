from typing import Optional

from starlette.config import Config
from starlette.datastructures import Secret


config = Config()

# whether the application is in development mode.
DEBUG: bool = config("FASTAPI_DEBUG", cast=bool, default=True)

# sqlalchemy database url.
DATABASE_URL: str = config("DATABASE_URL", cast=str)

# elasticsearch configuration.
ELASTICSEARCH_URL: str = config("ELASTICSEARCH_URL", cast=str)

# mail client host name.
MAIL_HOST: str = config("MAIL_HOST", cast=str)

# mail client port.
MAIL_PORT: int = config("MAIL_PORT", cast=int)

# mail client auth username.
MAIL_USERNAME: Optional[str] = config("MAIL_USERNAME", cast=str, default=None)

# mail client auth password.
MAIL_PASSWORD: Optional[Secret] = config("MAIL_PASSWORD", cast=Secret, default=None)

# mail client sender address.
MAIL_SENDER: Optional[str] = config("MAIL_SENDER", cast=str, default=None)
