import functools

from flask import request


def log_and_validate(func):
    """
    Example of decorator. Not used right now anywhere.
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        print("In Decorator")

        print(request.get_json())
        value = func(*args, **kwargs)
        print("After executing function")
        # Do something after

        return value

    return wrapper_decorator
