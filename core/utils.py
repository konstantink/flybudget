# coding=UTF-8


__author__ = 'Konstantin Kolesnikov'


from functools import wraps

from django.core.cache import cache
from django.http import HttpRequest


def cache_it(key):
    def wrapped(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[1]
            if request.user.is_authenticated():
                print('hello')
            # if isinstance(request, HttpRequest):
            #     request.COOKIES.
            return func(*args, **kwargs)
        return wrapper
    return wrapped