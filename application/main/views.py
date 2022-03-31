from flask import *
from application.utils import *
from application.models import *
# from application import current_user, login_user, logout_user, login_required
# from application import limiter
from application.main import main
import math

@main.route('/')
def index():
	page = request.args.get('page')
	lm = 16
	off = (int(page)-1)*lm  if page != None and page != 0 else 0
	phones = Phones.query.limit(lm).offset(off).all()
	l = Phones.query.count()
	pages = math.ceil(l / lm) 
	return render_template('index.html', phones=phones, pages=pages, active_page=off if off >= 1 else 1)


@main.route('/product/<id>')
def product(id):
	try:
		phone = Phones.query.filter_by(id=id).first()
		phone.id
		return render_template('product.html', phone=phone)
	except:
		return 'wronge product id'


@main.route('/test')
def test():
	return render_template('test.html')


@main.route('/test-data', methods=['POST'])
def test_post():
	_id = request.form.get('name')
	print(request.form.to_dict())
	print('in fetch bros')
	return {'msg':'good to go ' + str(_id)}
