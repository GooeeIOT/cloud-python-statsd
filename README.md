# cloud-python-statsd

Abstraction of statsd so that all [python] clients initialize and use the same statsd API and
utilities.

Currently, this amounts to a basic wrapper around the
[datadogpy](https://github.com/DataDog/datadogpy) library, but the API into the StatsD class is
standardized and will be patched to match assuming a new library is used as to not break existing
clients. The [datadogpy](https://github.com/~/datadogpy) library is used since it has tag support.

## Installing

```shell
pip install git@github.com:GooeeIOT/cloud-python-statsd.git
```

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

start_time = time.perf_counter()
ms = int((time.perf_counter() - start_time) * 1000)

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
initialize(host='localhost', namespace='my_metric_name', global_tags=['foo:bar'])
```

### Get More Info

Check out https://datadogpy.readthedocs.io/en/latest/
