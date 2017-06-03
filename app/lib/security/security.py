import flask
import functools

import AuthManager
import security_utils

security = flask.Blueprint('security', __name__)
auth_manager = AuthManager.AuthManager('dojo_website')

def login_required(admin_required=False, developer_required=False):
    def actual_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            flask.session['next'] = flask.request.url

            if is_logged_in(admin_required, developer_required):
                return function(*args, **kwargs)
            else:
                return flask.redirect(flask.url_for('security.login_form'))
        return wrapper
    return actual_decorator

def is_logged_in(admin_required=False, developer_required=False):
    username = flask.session.get('username')

    if not username:
        return False
    elif developer_required and auth_manager.is_developer(username):
        return True
    elif admin_required and auth_manager.is_admin(username):
        return True
    elif not (admin_required or developer_required) and auth_manager.is_registered(username):
        return True
    elif (admin_required and not auth_manager.is_admin(username)) or (developer_required and not auth_manager.is_developer(username)):
        return False
    else:
        flask.session.pop('username')
        return False

@security.route('/logged_in/')
def logged_in():
    return flask.jsonify(result=True if flask.session.get('username') else False)

@security.route('/testing/register/')
def register_form():
    if is_logged_in():
        return flask.redirect(flask.url_for('public_views.home'))
    else:
        return flask.render_template('register.html')

@security.route('/testing/register/', methods=['POST'])
def register():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    confirm_password = flask.request.form.get('confirm_password')

    if not username or not password or not confirm_password:
        flask.flash('Please fill out all fields!')
        return flask.redirect(flask.url_for('security.register_form'))

    results = auth_manager.register(username, password, confirm_password)
    flask.flash(results[1])

    if results[0]:
        return flask.redirect(flask.url_for('security.login_form'))
    else:
        return flask.redirect(flask.url_for('security.register_form'))

@security.route('/testing/login/')
def login_form():
    if is_logged_in():
        return flask.redirect(flask.url_for('public_views.home'))
    else:
        return flask.render_template('login.html')

@security.route('/testing/login/', methods=['POST'])
def login():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    if not username or not password:
        flask.flash('Please fill out all fields!')
        return flask.redirect(flask.url_for('security.login_form'))
    else:
        results = auth_manager.login(username, password)

        if results[0]:
            flask.session['username'] = username
            return security_utils.redirect_back()
        else:
            flask.flash(results[1])
            return flask.redirect(flask.url_for('security.login_form'))

@security.route('/testign/logout/')
def logout():
    if is_logged_in():
        flask.session.pop('username')

        if 'next' in flask.session:
            flask.session.pop('next')

    return flask.redirect(flask.url_for('public_views.home'))
