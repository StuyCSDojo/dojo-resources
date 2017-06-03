import functools
import time

def format_announcement(username, title, body):
    localtime = time.strftime('%c', time.localtime())
    announcement_html = '<h4>{title}</h4>\n<p class="condensed light a_info">Posted by {username} on {localtime}</p>\n<p>{body}</p>'
    return announcement_html.format(title=title, username=username, localtime=localtime, body=body)

def log_name(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        formatted_kwargs = ','.join(kwargs.values())
        print '{0}({1}{2})'.format(function.func_name, str(*args), formatted_kwargs)
        return function(*args, **kwargs)
    return inner
