from unittest import TestCase
from tape import Tape

class TestTape(TestCase):

    def test_initially_blank_head(self):
        t = Tape()
        self.assertEqual(t.read(), None)

    def test_all_blanks(self):
        t = Tape()
        t.shift_left()
        t.shift_left()
        t.shift_left()
        t.shift_left()
        self.assertEqual(t.read(), None)

        t2 = Tape()
        t.shift_right()
        t.shift_right()
        t.shift_right()
        t.shift_right()
        self.assertEqual(t.read(), None)
