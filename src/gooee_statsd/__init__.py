from datadog import initialize as dd_initialize, DogStatsd


name = 'gooee_statsd'


class StatsDClient(DogStatsd):

    # Make the api act like the "core" statsd API so we can switch of datadog easily if needed.
    incr = DogStatsd.increment
    decr = DogStatsd.decrement
    timer = DogStatsd.timed


def initialize(host: str, namespace: str, port: int = 8125, **kwargs):
    """
    Initialize a statsd client.

    It's advised to run this init only once per app execution and to surround this call at the
    caller site with STATSD_ENABLED.
    """
    # Monkeypatch the datadog statsd lib so that the "defaults" are auto supplied.
    dd_initialize(statsd_host=host, namespace=namespace, statsd_port=port, **kwargs)


statsd = StatsDClient()
