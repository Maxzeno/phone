from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, Length 


class SignupForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    phone_number = StringField('Phone number')
    first_name = StringField('First name')
    last_name = StringField('Last name')


class SigninForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')



class ForgotPasswordForm(FlaskForm):
    email = StringField('Email')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Password')
    confirm_password = PasswordField('Again')

class EmptyForm(FlaskForm):
    pass

