from flask import Blueprint

admin_section = Blueprint('admin_section', __name__, template_folder='templates')

from . import views
