import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("1", "2", "3")

    def test_check_in_guest(self):
        pass