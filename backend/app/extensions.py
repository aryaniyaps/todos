from typing import Optional

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_httpauth import HTTPTokenAuth

from app.core.security import check_auth_token
from app.models.users import User


cors = CORS()
migrate = Migrate()
db = SQLAlchemy()
mail = Mail()
auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token: str) -> Optional[User]:
    return check_auth_token(token=token)