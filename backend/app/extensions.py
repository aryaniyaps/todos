from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager


cors = CORS()
migrate = Migrate()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()