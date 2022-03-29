from flask import *
from application.utils import *
from application.models import *
from application.forms import EmptyForm
from application import current_user, login_user, logout_user, login_required
# from application import limiter
from application.user import user

from werkzeug.utils import secure_filename
import os


@user.route('/dashboard')
@login_required
def dashboard():
	phones = Phones.query.all()
	return render_template('dashboard.html', phones=phones)


@user.route('/add-phone', methods=["GET", "POST"])
@login_required
def add_phone():
	form = EmptyForm()
	if request.method == 'POST':
		print(request.files)
		print(request.form)
		print(dir(request))
		print(dir(request.form))
		# file = request.files['file']
		print(request.content_length, request.content_type)
		file = request.form['phone_image']

		print(file)
		filename = secure_filename(file)
		print(filename)
		file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
		return render_template('add_phone.html', form=form)
	return render_template('add_phone.html', form=form)


@user.route('/cart')
@login_required
def cart():
	phones = Phones.query.all()
	return render_template('cart.html', phones=phones)

