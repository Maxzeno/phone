from flask import *
from application.utils import *
from application.models import *
# from application import current_user, login_user, logout_user, login_required
# from application import limiter
from application.main import main
import math
import json
from random import randint



@main.route('/')
def index():
	page = request.args.get('page')
	lm = 16
	off = (int(page)-1)*lm  if page != None else 0
	phones = Phones.query.limit(lm).offset(off).all()
	l = Phones.query.count()
	pages = math.ceil(l / lm) 

	cart = request.cookies.get('cart')
	if cart:
		dict_cart = json.loads(cart)
		list_cart = list(dict_cart.keys())
		lst_cart = [ int(i) for i in list_cart ]
	else:
		lst_cart = {}

	return render_template('index.html', phones=phones, pages=pages, active_page=int(page) if page != None else 1, lst_cart=lst_cart, l=len(lst_cart))


# @main.route('/create-it')
# def create_it():

# 	prices = [35250, 204450, 198000, 63300, 8870]
# 	phone_image_fronts = ['51vf1R1wS9L._AC_UY218_.jpg', '71DCZOdq92S._AC_UY218_ (1).jpg', '71RxOftVoQL._AC_UY218_.jpg', '618LuqyIX6L._AC_UY218_.jpg']
	
# 	descriptions = ['LG Stylo 6 (64GB, 4GB) 6.8", w/Built-in Stylus Pen, 4000mAh Battery, 4G LTE GSM T-Mobile Unlocked (AT&T, Metro, Straight Talk) US Model - LM-Q730TM (128GB SD Bundle, White)',
# 	'Samsung Galaxy A12 (A127F) 128GB Dual SIM, GSM Unlocked, (CDMA Verizon/Sprint Not Supported) Smartphone International Version (Fast Car Charger Bundle) No Warranty (Blue)',
# 	'Google Pixel 6 Pro - 5G Android Phone - Unlocked Smartphone with Advanced Pixel Camera and Telephoto Lens - 128GB - Stormy Black',
# 	'Nokia G50 5G | Android 11 | Unlocked Smartphone | US Version | 4/128GB | 6.82-Inch Screen | 48MP Triple Camera | Ocean Blue',
# 	'Samsung Galaxy A12 (64GB, 4GB) 6.5" HD+, Quad Camera, 5000mAh Battery, Dual SIM GSM Unlocked Global 4G Volte (T-Mobile, AT&T, Metro) International Model A125M/DS (64GB SD Bundle, Black)',
# 	'SAMSUNG Galaxy S20 FE 5G Factory Unlocked Android Cell Phone 128GB US Version Smartphone Pro-Grade Camera 30X Space Zoom Night Mode, Cloud Navy',
# 	'OnePlus Nord N100 Midnight Frost Unlocked Smartphone​, 4GB+64GB, US Version, Model BE2011',
# 	'Moto G Power | 2021 | 3-Day battery | Unlocked | Made for US by Motorola | 3/32GB | 48MP Camera | Silver',
# 	'Blackview Android Phone, A80, 4G Dual sim Cell Phones, Bundle Android 10 OS 2GB+16GB ROM Unlocked Blackview Smartphones, 6.21in HD+, Fingerprint Face Detection, 4200mAh Capacity Battery tmobile Phone',
# 	'Latest Android 11 Phone, Ulefone Note 6 Unlocked Smartphone, 6.1” HD+ Full Screen, Quad-core 1GB+32GB Mobile Phone, 3300mAh Battery, Face Unlock, AI Camera 5MP+2MP Cell Phones- Purple']


# 	names = ['Iphone 12', 'Samsung s22 ultra', 'Itel p32', 'Geonee f102', 'Google pixel 6', 'Iphone 13 pro max', 'Samsung a2 core']
# 	brands = ['Apple', 'Samsung', 'Tecno', 'Itel', 'Infinix', 'Geonee', 'Google']

# 	for phone_image_front in phone_image_fronts:
# 		for description in descriptions:					
# 			phone = Phones(
# 				brand = brands[randint(0, len(brands)-1)],
# 				description = description,
# 				phone_image_front = phone_image_front,
# 				name = names[randint(0, len(names)-1)],
# 				price = prices[randint(0, len(prices)-1)]
# 			)
# 			db.session.add(phone)


# 	db.session.commit()

# 	return 'done'


@main.route('/product/<id>')
def product(id):
	phone = Phones.query.filter_by(id=id).first()
	if not phone:
		return 'no product with this id'

	cart = request.cookies.get('cart')
	if cart:
		dict_cart = json.loads(cart)
		list_cart = list(dict_cart.keys())
		lst_cart = [ int(i) for i in list_cart ]
	else:
		lst_cart = {}
		
	return render_template('product.html', lst_cart=lst_cart, phone=phone, l=len(lst_cart))


@main.route('/about')
def about():
	return render_template('about.html')


@main.route('/contact')
def contact():
	return render_template('contact.html')




@main.route('/test')
def test():
	return render_template('test.html')


@main.route('/test-data', methods=['POST'])
def test_post():
	_id = request.form.get('name')
	print(request.form.to_dict())
	print('in fetch bros')
	return {'msg':'good to go ' + str(_id)}




"""
flask-admin==1.6.0
Flask==1.0.2
Flask-Login==0.4.1
Flask-Migrate==2.4.0
Flask-SQLAlchemy==2.4.1
passlib==1.7.2
WTForms==2.2.1



"""