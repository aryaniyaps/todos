from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

__all__ = ("cache", "cors", "db", "migrate")


cors = CORS()
cache = Cache()
migrate = Migrate()
db = SQLAlchemy()
