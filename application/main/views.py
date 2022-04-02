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
	off = (int(page)-1)*lm  if page != None else 0
	phones = Phones.query.limit(lm).offset(off).all()
	l = Phones.query.count()
	pages = math.ceil(l / lm) 
	return render_template('index.html', phones=phones, pages=pages, active_page=int(page) if page != None else 1)


@main.route('/product/<id>')
def product(id):
	try:
		phone = Phones.query.filter_by(id=id).first()
		phone.id
		return render_template('product.html', phone=phone)
	except:
		return 'wronge product id'



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