import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Georgia Hogan", "Noah Thomson", "Carter Thomson")

def test_guest_has_name(self):
    self.assertEqual("Georgia Hogan", self.guest.name)

    