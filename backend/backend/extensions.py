from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail


__all__ = ("cors", "db", "migrate", "mail")


cors = CORS()
migrate = Migrate()
db = SQLAlchemy()
mail = Mail()