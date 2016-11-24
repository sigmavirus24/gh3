"""Collection of attrs conversion functions and validators."""
import datetime

NOT_PROVIDED = object()


def isodatetime(value):
    if value is NOT_PROVIDED:
        return value

    date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    return date.replace(tzinfo=UTC())


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
