from datetime import datetime
from flask import make_response, redirect, render_template, session, url_for
from functools import wraps, update_wrapper
from passlib.hash import argon2

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response    
    return update_wrapper(no_cache, view)

def redirect_back():
    destination = session.get('next')
    return redirect(destination) if destination else redirect(url_for('public_views.home'))

def secure_hash_password(password):
    return argon2.using(rounds=12).hash(password)
