import os
import time

from datadog import initialize as dd_initialize, DogStatsd


name = 'gooee_statsd'


def statsd_enabled(func):
    """Short circuit a function if statsd is not enabled."""
    def function_wrapper(*args, **kwargs):
        if not os.getenv('STATSD_ENABLED'):
            return
        func(*args, **kwargs)
    return function_wrapper


class StatsDClient(DogStatsd):

    @statsd_enabled
    def increment(self, *args, **kwargs):
        super().increment(*args, **kwargs)

    @statsd_enabled
    def decrement(self, *args, **kwargs):
        super().decrement(*args, **kwargs)

    @statsd_enabled
    def timed(self, *args, **kwargs):
        super().timed(*args, **kwargs)

    # Make the api act like the "core" statsd API so we can switch off datadog easily if needed.
    incr = DogStatsd.increment
    decr = DogStatsd.decrement
    timer = DogStatsd.timed


@statsd_enabled
def initialize(host: str, namespace: str, port: int = 8125, **kwargs) -> None:
    """
    Initialize a statsd client.

    It's advised to run this init only once per app execution and to surround this call at the
    caller site with STATSD_ENABLED.
    """
    # Monkeypatch the datadog statsd lib so that the "defaults" are auto supplied.
    dd_initialize(statsd_host=host, namespace=namespace, statsd_port=port, **kwargs)


# Create handle to statsd. This is what is used by consumer apps.
statsd = StatsDClient()


def timer_helper(name: str, t0: float) -> None:
    """
    Abstract how we do timings so the caller just needs to supply a name and initial time.

    t0 should be a timer.perf_counter()
    """
    ms = int((time.perf_counter() - t0) * 1000)
    statsd.timer(name, ms)
