from flask import *
from application.utils import *
from application.models import *
from application.forms import SignupForm, SigninForm, ForgotPasswordForm, ChangePasswordForm
from flask_login import current_user, login_user, logout_user, login_required
# from application import limiter
from application.auth import auth
from shortuuid import ShortUUID
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import smtplib
import uuid
from email.message import EmailMessage



@auth.route('/signup', methods=['GET','POST'])
# @limiter.limit("10 per minute")
def signup():
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	form = SignupForm()

	if request.method == 'POST' and form.validate_on_submit():
		logout_user()
		email = form.email.data
		password = form.password.data
		phone_number = form.phone_number.data
		first_name = form.first_name.data
		last_name = form.last_name.data

		found_email = User.query.filter_by(email=email).first()

		if found_email:
			flash(f'Email address already exists')
			return render_template('signup.html', email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, form=form, l=l)

		elif len(password) < 8 or len(password) > 50:
			flash('Password should be between 8 and 50 characters')
			return render_template('signup.html', email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, form=form, l=l)

		elif password.isnumeric() or password.isalpha():
			flash('Password should be alphanumeric')
			return render_template('signup.html', email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, form=form, l=l)

		else:
			password_hash = generate_password_hash(form.password.data, method='sha256')
			new_user = User(email=email,password=password_hash) 
			db.session.add(new_user)
			db.session.commit()

			_id = User.query.filter_by(email=email).first().id
			return redirect(url_for('auth.confirm_token', user_id=_id))


	return render_template('signup.html', form=form, l=l)


@auth.route('/confirm-token/<user_id>')
# @limiter.limit("10 per minute")
def confirm_token(user_id):
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	# try:
	user = User.query.filter_by(id=user_id).first()
	if user and user.suspended == False:
		s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

		token = s.dumps(user_id, salt='email-confirm')
		link = url_for('auth.confirm_email', token=token, _external=True)

		if request.host != '127.0.0.1:5000':
			msg = EmailMessage()
			msg['Subject'] = 'Confirmation email'
			msg['From'] = 'nwaegunwaemmauel@gmail.com'
			msg['To'] = user.email

			msg.set_content(f'Your confirmation link  {link}')
			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				smtp.login('nwaegunwaemmauel@gmail.com', 'yllzkejaxzhmpeuc')
				smtp.send_message(msg)
				smtp.quit()

				return render_template('status_msg.html', title='Confirm email', msg=f'Comfirm your email. <a href="/confirm-token/{user_id}">Resend</a>', l=l)


		with smtplib.SMTP('localhost', 1025) as smtp:

			subject = 'Confirmation email' 
			body = f'Your confirmation link  {link}'
			msg = f'Subject: {subject}\n\n{body}'
			smtp.sendmail('nwaegunwaemmauel@gmail.com', user.email, msg)
			smtp.quit()
			return render_template('status_msg.html', title='Comfirm email', msg=f'Comfirm your email. <a href="/confirm-token/{user_id}">Resend</a>', l=l)

	# except Exception as e:
	# 	print(e)
	# 	return render_template('status_msg.html', title='Technical Issues', msg=f'We experienced Technical Issues. <a href="/confirm-token/{user_id}">Retry</a>')



       
@auth.route('/confirm-email/<token>')
# @limiter.limit("10 per minute")
def confirm_email(token):
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	
	s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

	try:
		user_id = s.loads(token, salt='email-confirm', max_age=200000)
		user = User.query.filter_by(id=user_id).first()
		user.confirmed_email = True
		db.session.commit()
		return render_template('status_msg.html', title='Email confirmed', msg=f'Email confirmed you can now. <a href="/signin">signin</a>', l=l)


	except SignatureExpired:
		user_id = User.query.filter_by(id=user_id).first().id
		return render_template('status_msg.html', title='Token expired', msg=f'Token expired. <a href="/confirm-token/{user_id}">Resend</a>', l=l)



@auth.route('/signin', methods=['GET','POST'])
# @limiter.limit("10 per minute")
def signin():
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	form = SigninForm()

	if request.method == 'POST' and form.validate_on_submit():
		logout_user()

		email = form.email.data
		password = form.password.data

		user = User.query.filter_by(email=email).first()

		if not user or not check_password_hash(user.password, password):
			flash('Invalid login')
			return render_template('signin.html', email=email, form=form, l=l)                

		elif user.confirmed_email == False :
			return redirect(url_for('auth.confirm_token', user_id=user.id))

		elif user.suspended == True :
			flash('you are suspended')
			return render_template('signin.html', email=email, form=form, l=l)

		elif user.confirmed_email == True and check_password_hash(user.password, password) and user.suspended == False:  
			login_user(user)
			if session.get('next') == None:
				return redirect(url_for('user_section.explore'))
			elif session.get('next') != None:
				return redirect(session.get('next'))

		else:
			return render_template('status_msg.html', title='Technical Issues', msg=f'We experience a Technical Issues. <a href="/confirm-token/{user_id}">Retry</a>', l=l)


	session.pop('next', None)
	session['next'] = request.args.get('next')
	return render_template('signin.html', form=form, l=l)



@auth.route('/signout')
# @limiter.limit("10 per minute")
def signout():
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	logout_user()
	return redirect(url_for('auth.signin'))


##################################

@auth.route('/forgot-password', methods=['GET','POST'])
# @limiter.limit("10 per minute")
def forgot_password():
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	form = ForgotPasswordForm()
	if request.method == 'POST' and form.validate_on_submit():
		email = form.email.data
		s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
		user = User.query.filter_by(email=email).first()

		if user and user.suspended == False:
			try:
				token = s.dumps(user.id, salt='email-reset')
				link = url_for('auth.change_password', token=token, _external=True)

				if request.host != '127.0.0.1:5000':
					msg = EmailMessage()
					msg['Subject'] = 'Confirmation email'
					msg['From'] = 'nwaegunwaemmauel@gmail.com'
					msg['To'] = email
					msg.set_content(f'Your confirmation link  {link}')
					with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
						smtp.login('nwaegunwaemmauel@gmail.com', 'yllzkejaxzhmpeuc')
						smtp.send_message(msg)
						return render_template('status_msg.html', title='Comfirm email', msg='Comfirmation email has been sent to try again <a href="/change-password">click here</a>', l=l)
				
				with smtplib.SMTP('localhost', 1025) as smtp:

					subject = 'Confirmation email' 
					body = f'Your confirmation link  {link}'
					msg = f'Subject: {subject}\n\n{body}'
					smtp.sendmail('nwaegunwaemmauel@gmail.com', user.email, msg)
					return render_template('status_msg.html', title='Comfirm email', msg='Comfirmation email has been sent to try again <a href="/change-password">click here</a>', l=l)

			except:
				return render_template('status_msg.html', title='Email Server Off', msg="""We can't send confirmation email now <a href="/change-password">try again</a>""", l=l)

		else:
			return render_template('status_msg.html', title='Comfirm email', msg='Comfirmation email has been sent to try again <a href="/change-password">click here</a>', l=l)

	return render_template('forgot_password.html', form=form, l=l)



@auth.route('/change-password/<token>', methods=['GET','POST'])
# @limiter.limit("10 per minute")
def change_password(token):
	cart = request.cookies.get('cart')
	if cart:
		l = len(list(json.loads(cart)))
	else:
		l = 0
	form =  ChangePasswordForm()
	if request.method == 'POST' and form.validate_on_submit():
		try:
			s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
			user_id = s.loads(token, salt='email-reset', max_age=200000)
			user = User.query.filter_by(id=user_id).first()

			if user and user.suspended == False:
				password = form.password.data
				confirm_password = form.confirm_password.data
				if password != confirm_password:
					flash("The two Passwords did'nt match")
					return render_template('change_password.html', token=token, form=form, l=l)

				elif len(password) < 8 or len(password) > 50:
					flash('Password should be between 8 and 50 characters')
					return render_template('change_password.html', token=token, form=form, l=l)

				elif password.isnumeric() or password.isalpha():
					flash('Password should be alphanumeric')
					return render_template('change_password.html', token=token, form=form, l=l)

				else:
					password_hash = generate_password_hash(password, method='sha256')
					User.query.filter_by(id=user_id).first().password = password_hash
					db.session.commit()

					return render_template('status_msg.html', title='Password change', msg='Password has been change. <a href="/signin">signin</a>', l=l)
			else:
				return render_template('change_password.html',token=token, form=form, l=l)
		except SignatureExpired:
			return render_template('status_msg.html', title='Token expired', msg='Token expired to try again <a href="/change-password">click here</a>', l=l)

	return render_template('change_password.html',token=token, form=form, l=l)

            
