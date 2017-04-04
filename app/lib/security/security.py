from flask import (Blueprint, flash, get_flashed_messages, jsonify,
                   redirect, render_template, request, session, url_for)
from functools import wraps

from lib.database import DBManager
from utils import redirect_back

security = Blueprint('security', __name__)
db_manager = DBManager('dojo_website')

def login_required(admin_required = False, developer_required = False):
    def actual_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if is_logged_in(admin_required, developer_required):
                return function(*args, **kwargs)
            else:
                session['next'] = request.url
                return redirect(url_for('security.login_form'))
        return wrapper
    return actual_decorator

def is_logged_in(admin_required = False, developer_required = False):
    username = session.get('username')
    
    if not username:
        return False
    elif developer_required and db_manager.is_developer(username):
        return True
    elif admin_required and db_manager.is_admin(username):
        return True
    elif not (admin_required or developer_required) and db_manager.is_registered(username):
        return True
    elif (admin_required and not db_manager.is_admin(username)) or (developer_required and not db_manager.is_developer(username)):
        return False
    else:
        session.pop('username')
        return False

@security.route('/testing/logged_in/')
def logged_in():
    print session.get('username')
    return jsonify(result=True if session.get('username') else False)
    
@security.route('/testing/register/')
def register_form():
    if is_logged_in():
        return redirect(url_for('public_views.home'))
    else:
        return render_template('register.html')
            
@security.route('/testing/register/', methods = ['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    if not username or not password or not confirm_password:
        flash('Please fill out all fields!')
        return redirect(url_for('security.register_form'))

    results = db_manager.register(username, password, confirm_password)
    flash(results[1])

    if results[0]:
        return redirect(url_for('security.login_form'))
    else:
        return redirect(url_for('security.register_form'))

@security.route('/testing/login/')
def login_form():
    if is_logged_in():
        return redirect(url_for('public_views.home'))
    else:
        return render_template('login.html')

@security.route('/testing/login/', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        flash('Please fill out all fields!')
        return redirect(url_for('security.login_form'))
    else:
        results = db_manager.login(username, password)
        
        if results[0]:
            session['username'] = username
            return redirect_back()
        else:
            flash(results[1])
            return redirect(url_for('security.login_form'))

@security.route('/testing/logout/')
def logout():
    if is_logged_in():
        session.pop('username')

        if 'next' in session:
            session.pop('next')

    return redirect(url_for('public_views.home'))
