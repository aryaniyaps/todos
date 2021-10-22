from environs import Env


env = Env()
env.read_env()

# flask core configuration.
SECRET_KEY = env.str("SECRET_KEY")
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=False)
ENV = env.str("FLASK_ENV", default="development")
DEBUG = env.bool("FLASK_DEBUG", default=True)

# sqlalchemy configuration.
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask-caching configuration.
CACHE_TYPE = env.str("CACHE_TYPE")
CACHE_DEFAULT_TIMEOUT = env.int("CACHE_DEFAULT_TIMEOUT")
CACHE_REDIS_URL = env.str("CACHE_REDIS_URL")
