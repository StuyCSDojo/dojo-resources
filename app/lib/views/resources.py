from flask import Blueprint, current_app, Flask
from os.path import join

from lib.util import log_name

resources = Blueprint('resources', __name__)

@resources.route('/testing/public_resources/knights-tour-sketchpad/')
@resources.route('/testing/public_resources/knights-tour-sketchpad/<path:filename>')
@log_name
def knight_tour(filename = 'index.html'):
    path = join('useful_links/knights-tour-sketchpad', filename)
    return current_app.send_static_file(path)

@resources.route('/testing/public_resources/nqueens-sketchpad/')
@resources.route('/testing/public_resources/nqueens-sketchpad/<path:filename>')
@log_name
def nqueens_sketchpad(filename = 'index.html'):
    path = join('useful_links/nqueens-sketchpad', filename)
    return current_app.send_static_file(path)
