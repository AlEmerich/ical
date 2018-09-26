from urllib.request import urlopen
from icalendar import Calendar


class Ical(object):

    def __init__(self, path=None, url=True):
        content = None

        if url:
            content = urlopen(path).read().decode('iso-8859-1')
        else:
            content = open(path, 'r').read()

        self.cal = Calendar.from_ical(content)
