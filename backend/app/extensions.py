from flask_login import LoginManager

from app.users.services import user_service


login_manager = LoginManager()
login_manager.user_loader(user_service.get_user)