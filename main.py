import argparse
from ical.utilities import Ical

FORMAT_DATE = "%Y-%m-%d"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", required=True, type=str)
    parser.add_argument("-y", required=True, type=int)
    parser.add_argument("-m", required=True, type=int)
    parser.add_argument("-d", required=True, type=int)
    args = parser.parse_args()

    calendar = Ical(args.path)
    events = calendar.get_next_bin(args.y, args.m, args.d)
    for i, e in enumerate(events):
        print("***************\nEvent " + str(i))
        calendar.pretty_print(e)
