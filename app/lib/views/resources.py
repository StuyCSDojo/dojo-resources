import flask
import os.path

from lib.security import security, security_utils
from lib.utils import utils

resources_views = flask.Blueprint('resources', __name__)

@resources_views.route('/public_resources/knights-tour-sketchpad/')
@resources_views.route('/public_resources/knights-tour-sketchpad/<path:filename>')
@utils.log_name
def knight_tour(filename='index.html'):
    path = os.path.join('useful_links/knights-tour-sketchpad', filename)
    return flask.current_app.send_static_file(path)

@resources_views.route('/public_resources/nqueens-sketchpad/')
@resources_views.route('/public_resources/nqueens-sketchpad/<path:filename>')
@utils.log_name
def nqueens_sketchpad(filename='index.html'):
    path = os.path.join('useful_links/nqueens-sketchpad', filename)
    return flask.current_app.send_static_file(path)

@resources_views.route('/testing/private/resources/')
@resources_views.route('/testing/private/resources/<path:filename>')
@utils.log_name
@security_utils.nocache
@security.login_required(developer_required=True)
def private_resources(filename='index.html'):
    path = os.path.join('private_resources/build/html', filename)
    return flask.current_app.send_static_file(path)

@resources_views.route('/testing/public/resources/')
@resources_views.route('/testing/public/resources/<path:filename>')
@utils.log_name
@security_utils.nocache
@security.login_required(developer_required=True)
def public_resources(filename='index.html'):
    path = os.path.join('public_resources/build/html', filename)
    return flask.current_app.send_static_file(path)
