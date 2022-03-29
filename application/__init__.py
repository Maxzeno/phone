from flask import *
from application.config import Config

from sqlalchemy import func

from datetime import *

from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)
login_manager = LoginManager()
migrate = Migrate()
bootstrap = Bootstrap()


login_manager.login_view = 'auth.signin'

def create_app(config_class=Config):
	"""Returns an initialized Flask application."""
	app = Flask(__name__)
	app.config.from_object(Config)
	app.permanent_session_lifetime = timedelta(days=365)

	db.init_app(app)
	login_manager.init_app(app)
	migrate.init_app(app, db)
	limiter.init_app(app)
	bootstrap.init_app(app)
	

	from application.user import user
	from application.auth import auth
	from application.main import main
	from application.admin import admin


	app.register_blueprint(user) 
	app.register_blueprint(auth)
	app.register_blueprint(main)
	app.register_blueprint(admin)

	return app

