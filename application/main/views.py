from flask import *
from application.utils import *
from application.models import *
# from application import current_user, login_user, logout_user, login_required
# from application import limiter
from application.main import main
import math
import json

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

@main.route('/send-cart', methods=['POST'])
def send_cart():
	_id = request.form.get('id')

	number = request.form.get('number')
	cart = request.cookies.get('cart')
	if cart:
		dict_cart = json.loads(cart)
		if dict_cart.get(_id) and dict_cart.get(_id) == number:
			del dict_cart[_id]
			resp = make_response(jsonify({'msg': _id, 'status': 'remove'}))
			resp.set_cookie('cart', json.dumps(dict_cart), max_age=31557600)

			return resp

		dict_cart[_id] = number
		resp = make_response(jsonify({'msg': _id, 'status': 'add'}))
		resp.set_cookie('cart', json.dumps(dict_cart), max_age=31557600)
		return resp

	resp = make_response(jsonify({'msg': _id, 'status': 'add'}))
	resp.set_cookie('cart', json.dumps({_id: number}), max_age=31557600)
	return resp



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