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

    # Make the api act like the "core" statsd API so we can switch off datadog easily if needed.
    incr = DogStatsd.increment
    decr = DogStatsd.decrement
    timer = DogStatsd.timed


# Create handle to statsd. This is what is used by consumer apps.
statsd = StatsDClient()
