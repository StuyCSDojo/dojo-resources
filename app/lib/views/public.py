from flask import Blueprint, current_app, render_template
from os.path import join

from lib.database import DBManager
from lib.security.security import login_required
from lib.security.utils import nocache
from lib.util import log_name

public_views = Blueprint('public_views', __name__)
db_manager = DBManager('dojo_website')

@public_views.route('/testing/')
def home():
    return render_template('index.html')

@public_views.route('/testing/public/resources/')
@public_views.route('/testing/public/resources/<path:filename>')
@nocache
@login_required(developer_required=True)
def resources(filename='index.html'):
    path = join('public_resources/build/html', filename)
    return current_app.send_static_file(path)

