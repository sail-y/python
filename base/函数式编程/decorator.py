# coding=utf-8
import functools

__author__ = 'xiaomai'


def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text == None:
                print '%s %s():' % ('no text', func.__name__)
            else:
                print '%s %s():' % (text, func.__name__)
                return func(*args, **kw)

        return wrapper

    return decorator


@log()
def now():
    print('2016年02月24日16:57:09')


now()
