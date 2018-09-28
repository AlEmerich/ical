from urllib.request import urlopen
from icalendar import Calendar
import datetime
import sys


class Ical(object):
    """ Class holding an Icalendar object and
    add utilities function to access it.
    """
    def __init__(self, path=None):
        """Load an .ical text file.
        :param path: can be a file in disk or an url.
        """
        content = None

        try:
            content = urlopen(path).read().decode('iso-8859-1')
        except ValueError:
            content = open(path, 'r').read()

        self.cal = Calendar.from_ical(content)

    def pretty_print(self, event):
        """Pretty print event in the standard output
        """
        uid = str(event.get("UID").to_ical().decode("utf-8"))
        dtstart = str(event.get("DTSTART").dt)
        dtstamp = str(event.get("DTSTAMP").dt)
        summary = str(event.get("SUMMARY").to_ical().decode("utf-8"))
        print("UID:", uid,
              "\nDTSTART:", dtstart,
              "\nDTSTAMP", dtstamp,
              "\nSUMMARY", summary)

    def get_next_bin(self, year, month, day):
        """Retrieve the next bin collection given an input date.
        :param year: the year of the date to llok for.
        :param month: the month of the date to look for.
        :param day: the day of the date to look for.
        :return the next bin collection as list.
        """
        date = datetime.date(year, month, day)

        next_event = []
        diff_of_next = sys.maxsize

        for e in self.cal.walk("VEVENT"):
            for p in e.walk():
                # Get the difference between the specified date
                # and the one of the current event
                diff = (p.get("DTSTART").dt - date).days

                # check if the current is after
                if diff >= 0:
                    # check if it is closer than a previous found one
                    if diff <= diff_of_next:
                        # if it is not the same the previous found one,
                        # we can flush event previously found from our list
                        if diff != diff_of_next:
                            next_event.clear()
                            diff_of_next = diff
                        next_event.append(p)
        return next_event
