import os


def statsd_enabled(func):
    """Short circuit a function if statsd is not enabled."""
    def function_wrapper(*args, **kwargs):
        if not os.getenv('STATSD_ENABLED'):
            return
        func(*args, **kwargs)
    return function_wrapper