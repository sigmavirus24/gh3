"""Collection of attrs conversion functions and validators."""
import datetime

import attr

NOT_PROVIDED = object()


def isodatetime(value):
    if value is NOT_PROVIDED:
        return value

    date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    return date.replace(tzinfo=UTC())


def aliased(json_key, **kwargs):
    kwargs.setdefault('metadata', {})
    kwargs['metadata']['json_key'] = json_key
    return attr.ib(**kwargs)


class UTC(datetime.tzinfo):

    """Yet another UTC reimplementation, to avoid a dependency on pytz or
    dateutil."""

    ZERO = datetime.timedelta(0)

    def __repr__(self):
        return 'UTC()'

    def dst(self, dt):
        return self.ZERO

    def tzname(self, dt):
        return 'UTC'

    def utcoffset(self, dt):
        return self.ZERO
