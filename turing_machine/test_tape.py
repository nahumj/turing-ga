from unittest import TestCase
from tape import Tape

class TestTape(TestCase):

    def test_initially_blank_head(self):
        t = Tape()
        self.assertEqual(t.read(), None)

