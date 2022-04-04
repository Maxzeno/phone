from flask import Blueprint

user_section = Blueprint('user_section', __name__, template_folder='templates')

from . import views
