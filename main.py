from ical.utilities import Ical

if __name__ == "__main__":
    calendar = Ical(path="https://s3-eu-west-1.amazonaws.com/fs-downloads/GM/binfeed.ical")
    print(calendar.cal.content_lines())
