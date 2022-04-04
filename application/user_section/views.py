from flask import *
from application.utils import *
from application.models import *
from application.forms import EmptyForm
from application import current_user, login_user, logout_user, login_required#, images
# from application import limiter
from application.user_section import user_section

from werkzeug.utils import secure_filename
import os
import math
import json
from inspect import signature


@user_section.route('/explore')
@login_required
def explore():
	page = request.args.get('page')
	lm = 16
	off = (int(page)-1)*lm  if page != None else 0
	phones = Phones.query.limit(lm).offset(off).all()
	length_phones = Phones.query.count()
	pages = math.ceil(length_phones / lm) 

	cart = request.cookies.get('cart')
	if cart:
		dict_cart = json.loads(cart)
		list_cart = list(dict_cart.keys())
		lst_cart = [ int(i) for i in list_cart ]
	else:
		lst_cart = []

	return render_template('explore.html', phones=phones, pages=pages, active_page=int(page) if page != None else 1, lst_cart=lst_cart, l=len(lst_cart))


@user_section.route('/add-phone', methods=["GET", "POST"])
@login_required
def add_phone():
	form = AddPhoneForm()
	# if form.validate_on_submit():
	# 	filename = images.save(form.image.data)
	# 	return f'Filename: {filename}'
	return render_template('add_phone.html', form=form)


@user_section.route('/cart')
def cart():
	cart = request.cookies.get('cart')
	dict_cart = json.loads(cart)
	lst_cart = list(dict_cart.keys())

	cart = request.cookies.get('cart')
	dict_cart = json.loads(cart)

	phones = Phones.query.filter(Phones.id.in_(lst_cart)).all()
	return render_template('cart.html', phones=phones, l=len(dict_cart))


@user_section.route('/subdomain', subdomain='test')
def subdomain():
    return 'ur welcome my friend or bro to subdomain'

