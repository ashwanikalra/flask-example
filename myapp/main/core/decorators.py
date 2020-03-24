import functools


def log_and_validate(func):
    """
    Example of decorator. Not used right now anywhere.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before

        # start_time = time.process_time()
        #
        # value = func(*args, **kwargs)
        # duration = time.process_time()
        # Do something after

        pass

    return wrapper_decorator
