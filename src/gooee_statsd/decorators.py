import logging
import os

LOG = logging.getLogger('gooee_statsd')


def statsd_enabled(func):
    """Short circuit a function if statsd is not enabled."""
    def function_wrapper(*args, **kwargs):
        if not os.getenv('STATSD_ENABLED'):
            LOG.debug(f'STATSD_ENABLED is not set so skipping statsd operation: {args} {kwargs}')
            return
        func(*args, **kwargs)
    return function_wrapper
