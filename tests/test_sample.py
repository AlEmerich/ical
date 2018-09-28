import unittest
from ical.utilities import Ical

TEST_FILE = "tests/binfeed.ical"
TEST_URL = "https://s3-eu-west-1.amazonaws.com/fs-downloads/GM/binfeed.ical"

class TestIcal(unittest.TestCase):
    def test_file_loading(self):
        """Test if the load from disk.
        """
        try:
            cal = Ical(TEST_FILE)
        except:
            self.assertTrue(False)

    def test_url_loading(self):
        """Test the load from url.
        """
        try:
            cal = Ical(TEST_URL)
        except:
            self.assertTrue(False)

    def test_no_solution(self):
        """Test when there is no solutions.
        """
        calendar = Ical(TEST_FILE)
        events = calendar.get_next_bin(2020, 12, 25)
        self.assertTrue(not events)

    def test_one_bin(self):
        """Test when there is just one solution.
        """
        calendar = Ical(TEST_FILE)
        events = calendar.get_next_bin(2018, 1, 16)
        self.assertFalse(not events)
        self.assertEqual(1, len(events))

    def test_two_bin(self):
        """Test when there are two solutions.
        """
        calendar = Ical(TEST_FILE)
        events = calendar.get_next_bin(2018, 5, 28)
        self.assertFalse(not events)
        self.assertEqual(2, len(events))

    def test_regularity(self):
        uids = ["20180103T190905GMT-4437IlTejd@192.124.249.105",
                "20180103T190905GMT-4463fruaVC@192.124.249.105"]
        calendar = Ical(TEST_FILE)
        events = calendar.get_next_bin(2018, 5, 28)
        for e in events:
            uid = e.get("UID").to_ical().decode("utf-8")
            self.assertTrue(uid in uids)
