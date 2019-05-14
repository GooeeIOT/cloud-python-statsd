import logging

from datadog import api
from datadog.util.hostname import get_hostname

from gooee_statsd.client import StatsDClient, statsd
from gooee_statsd.decorators import statsd_enabled

name = 'gooee_statsd'

LOG = logging.getLogger('gooee_statsd')


@statsd_enabled
def initialize(
        host: str,
        namespace: str,
        port: int = 8125,
        host_name: str = None,
        use_default_route: bool = False
) -> None:
    """Initialize a statsd client."""
    LOG.debug('Initializing Gooee StatsD lib with host={host} port={port}')
    # Monkeypatch the datadog statsd lib so that the "defaults" are auto supplied.
    api._host_name = host_name if host_name is not None else get_hostname()
    api._api_host = host
    statsd.host = statsd.resolve_host(host, use_default_route)
    statsd.port = port
    statsd.namespace = namespace


def timer_helper(name: str, t0: float) -> None:
    """
    Abstract how we do timings so the caller just needs to supply a name and initial time.

    t0 should be a timer.perf_counter()
    """
    ms = int((time.perf_counter() - t0) * 1000)
    statsd.timer(name, ms)