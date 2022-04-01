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
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView


# from flask_uploads import configure_uploads, IMAGES, UploadSet



db = SQLAlchemy()

# from application.models import *

limiter = Limiter(key_func=get_remote_address)
login_manager = LoginManager()
migrate = Migrate()
bootstrap = Bootstrap()

# admin = Admin()

# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)

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
	# admin.init_app(app)



	from application.user import user
	from application.auth import auth
	from application.main import main
	from application.admin_user import admin_user


	app.register_blueprint(user) 
	app.register_blueprint(auth)
	app.register_blueprint(main)
	app.register_blueprint(admin_user)

	return app


