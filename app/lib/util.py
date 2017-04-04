from functools import wraps
from hashlib import sha512
from time import localtime, strftime, time

def hash_string(s):
    return sha512(s).hexdigest()
    
def log_name(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print func.func_name + '(' + str(*args) + str(','.join(kwargs.values())) + ')'
        return func(*args, **kwargs)
        
    return inner
