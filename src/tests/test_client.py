from gooee_statsd.client import StatsDClient


def test__sanitize_metric():
    cases = (
        ('foo:bar', 'foo_bar'),
        ('foo.bar:baz', 'foo.bar_baz'),
        ('foo.bar:baz', 'foo.bar_baz'),
    )
    for submitted, expected in cases:
        assert StatsDClient._sanitize_metric(submitted) == expected