# cloud-python-statsd

Abstraction of statsd so that all [python] clients initialize and use the same statsd API.

## Initialize StatsD Client

Initialize statsd with connection info that will be globally applied to further statsd calls.

```python
from gooee_statsd import initialize

initialize(host='localhost', namespace='my_app_name')
```

A `namespace` is prepended to *all* metrics. *This should be the app name* so that it's unique in
Grafana and other apps won't accidentally write to another app's metric.

## Using the StatsD Client

```python
from gooee_statsd import statsd

statsd.incr('my.metric.name')
```

## Get Fancy

### Timers

```python
import time
from gooee_statsd import statsd

start_time = time.time()
ms = int((time.time() - start_time) * 1000)

statsd.timing('my_metric_name', ms)
```

### Tag a Metric

```python
statsd.incr('my.metric.some_name', tags=['my_key:some'])
statsd.incr('my.metric.other_name', tags=['my_key:other'])
```

In Grafana, this will help you find all metric names tagged with `my_key=some_value_you_care_about`.

### Global Tags

Like a tagging for metrics, but automagically applied to all metrics.

```python
initialize(host='localhost', namespace='lyletest', global_tags=['foo:bar'])
```

### Get More Info

Check out https://datadogpy.readthedocs.io/en/latest/