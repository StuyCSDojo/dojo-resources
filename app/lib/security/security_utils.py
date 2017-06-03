import datetime
import flask
import functools
import passlib.hash

def nocache(view):
    @functools.wraps(view)
    def no_cache(*args, **kwargs):
        response = flask.make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return functools.update_wrapper(no_cache, view)

def redirect_back():
    destination = flask.session.get('next')
    return flask.redirect(destination) if destination else flask.redirect(flask.url_for('public_views.home'))

def secure_hash_password(password):
    return passlib.hash.argon2.using(rounds=12).hash(password)
