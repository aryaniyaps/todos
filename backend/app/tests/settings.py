from typing import Optional


# branding configuration.
PUBLIC_SITE_NAME: str = "Todos tests"

# app environment.
ENV: str = "development"

# whether debug features are enabled.
DEBUG: bool = True

# whether we are testing.
TESTING: bool = True

# session secret configuration.
SECRET_KEY: str = "secret"

# sqlalchemy database URL.
SQLALCHEMY_DATABASE_URI: str = "sqlite://"

# whether modifications are tracked.
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

# mail client host name.
MAIL_SERVER: str = "localhost"

# mail client port.
MAIL_PORT: int = 25

# whether the mail client should use tls.
MAIL_USE_TLS: bool = False

# mail client auth username.
MAIL_USERNAME: Optional[str] = None

# mail client auth password.
MAIL_PASSWORD: Optional[str] = None

# mail client sender address.
MAIL_DEFAULT_SENDER: Optional[str] = None
