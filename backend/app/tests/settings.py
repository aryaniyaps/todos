"""
Configuration options for tests.
"""

# branding configuration.
PUBLIC_SITE_NAME: str = "Todos tests"

# whether we are testing.
TESTING: bool = True

# session secret configuration.
SECRET_KEY: str = "secret"

# sqlalchemy database URL.
SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"

# whether modifications are tracked.
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

# disable mail sending.
MAIL_SUPPRESS_SEND: bool = True