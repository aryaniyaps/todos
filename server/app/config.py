from decouple import config


# whether the app is in development.
DEBUG = config("DEBUG", default=False, cast=bool)

# whether the app is in the test suite.
TESTING = config("TESTING", default=False, cast=bool)

# SQLAlchemy database URL.
DATABASE_URL = config("DATABASE_URL")

# app's secret key.
SECRET_KEY = config("SECRET_KEY")
