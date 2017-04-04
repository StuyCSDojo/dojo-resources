
from flask import Blueprint, current_app, render_template, redirect, request, session, url_for
from os.path import join

from lib.database import DBManager
from lib.security.security import login_required
from lib.security.utils import nocache
from lib.util import log_name

private_views = Blueprint('private_views', __name__)
db_manager = DBManager('dojo_website')

@private_views.route('/testing/private/resources/')
@private_views.route('/testing/private/resources/<path:filename>')
@log_name
@nocache
@login_required(developer_required=True)
def render_resources(filename='index.html'):
    path = join('private_resources/build/html', filename)
    return current_app.send_static_file(path)
