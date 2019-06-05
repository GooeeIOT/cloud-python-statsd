from datadog import DogStatsd

from gooee_statsd.decorators import statsd_enabled


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

    @staticmethod
    def _sanitize_metric(metric):
        """Prevent some common cases of "bad" metric names."""
        return metric.replace(':', '_')

    def increment(self, metric, value=1, tags=None, *args, **kwargs):
        metric = self._sanitize_metric(metric)
        return super().increment(metric, value, tags, *args, **kwargs)

    def decrement(self, metric, value=1, tags=None, *args, **kwargs):
        metric = self._sanitize_metric(metric)
        return super().decrement(metric, value, tags, *args, **kwargs)

    def timed(self, metric=None, tags=None, *args, **kwargs):
        metric = self._sanitize_metric(metric)
        return super().timed(metric, tags, *args, **kwargs)

    def timing(self, metric, value, tags=None, *args, **kwargs):
        metric = self._sanitize_metric(metric)
        return super().timing(metric, value, tags, *args, **kwargs)

    # Make the api act like the "core" statsd API so we can switch off datadog easily if needed.
    incr = increment
    decr = decrement
    timer = timing


# Create handle to statsd. This is what is used by consumer apps.
statsd = StatsDClient()
