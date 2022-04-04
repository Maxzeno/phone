from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, FileField
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

class AddPhoneForm(FlaskForm):
    image = FileField('image')
    name = StringField('Name')
    brand = StringField('Brand')
    description = TextAreaField('Description')
    color = StringField('Color')
    # some wont be tradition input some might  be like buttons 

class ContactUsForm(FlaskForm):
    email = StringField('Email')
    message = StringField('Message')

class NewsLetterForm(FlaskForm):
    email = StringField('Email')
