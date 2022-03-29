from flask import *
from application.utils import *
from application.models import *
# from application import current_user, login_user, logout_user, login_required
# from application import limiter
from application.main import main

@main.route('/')
def index():
	phones = Phones.query.all()
	return render_template('index.html', phones=phones)

