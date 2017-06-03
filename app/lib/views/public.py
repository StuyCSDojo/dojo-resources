import flask
import os.path

from lib.security import security, security_utils
from lib.utils import utils

public_views = flask.Blueprint('public_views', __name__)

@public_views.route('/')
@public_views.route('/testing/')
def home():
    return flask.render_template('index.html')
