from flask import Blueprint

admin_user = Blueprint('admin_user', __name__, template_folder='templates')

from . import views
