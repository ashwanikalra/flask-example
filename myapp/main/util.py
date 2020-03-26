import pstats
import sys
import time

from flask import request

try:
    from cProfile import Profile
except ImportError:
    from profile import Profile


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('{}  {} ms'.format(method.__name__, (te - ts) * 1000))
        return result

    return timed


def code_profiler(fn):
    """
    decorator to profile a given function for bottlenecks in the code.
    :param fn:
    :return:
    """

    def wrapped_func(*args, **kwargs):
        global cc_profiler
        # profile only if debug flag is true
        try:
            cc_profiler = Profile()
            result = cc_profiler.runcall(fn, *args, **kwargs)
        finally:
            # print(request.path)
            stats = pstats.Stats(cc_profiler, stream=sys.stdout)
            # stats.strip_dirs().sort_stats('cumulative', 'calls')
            stats.strip_dirs().sort_stats('time', 'calls')
            print("-" * 80, file=sys.stdout)
            print("PATH: {!r}".format(request.path), file=sys.stdout)
            stats.print_stats(10)
            print("-" * 80 + "\n", file=sys.stdout)
        return result

    return wrapped_func
