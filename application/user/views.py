from flask import *
from application.utils import *
from application.models import *
from application.forms import EmptyForm
from application import current_user, login_user, logout_user, login_required#, images
# from application import limiter
from application.user import user

from werkzeug.utils import secure_filename
import os
import math


@user.route('/explore')
@login_required
def explore():
	page = request.args.get('page')
	lm = 16
	off = (int(page)-1)*lm  if page != None and page != 0 else 0
	phones = Phones.query.limit(lm).offset(off).all()
	l = Phones.query.count()
	pages = math.ceil(l / lm) 
	return render_template('explore.html', phones=phones, pages=pages, active_page=off if off >= 1 else 1)


@user.route('/add-phone', methods=["GET", "POST"])
@login_required
def add_phone():
	form = AddPhoneForm()
	# if form.validate_on_submit():
	# 	filename = images.save(form.image.data)
	# 	return f'Filename: {filename}'
	return render_template('add_phone.html', form=form)


@user.route('/cart')
@login_required
def cart():
	phones = Phones.query.all()
	return render_template('cart.html', phones=phones)

