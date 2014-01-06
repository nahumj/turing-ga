from unittest import TestCase
from tape import Tape

class TestTape(TestCase):

    def test_initially_blank_head(self):
        t = Tape()
        self.assertEqual(t.read(), 0)

    def test_all_blanks(self):
        t = Tape()
        t.shift_left()
        t.shift_left()
        t.shift_left()
        t.shift_left()
        self.assertEqual(t.read(), 0)

        t2 = Tape()
        t2.shift_right()
        t2.shift_right()
        t2.shift_right()
        t2.shift_right()
        self.assertEqual(t2.read(), 0)

    def test_different_blank_symbol(self):
        t = Tape(blank_symbol=None)
        self.assertEqual(t.read(), None)

        t.shift_left()
        t.shift_left()
        t.shift_left()
        t.shift_left()
        self.assertEqual(t.read(), None)

        t2 = Tape(blank_symbol=None)
        t2.shift_right()
        t2.shift_right()
        t2.shift_right()
        t2.shift_right()
        self.assertEqual(t2.read(), None)

    def test_write(self):
        t = Tape()
        self.assertEqual(t.read(), 0)
        t.write(1)
        self.assertEqual(t.read(), 1)

    def test_write_shift(self):
        t = Tape()
        t.write(1)
        t.shift_left()
        self.assertEqual(t.read(), 0)
        t.shift_right()
        self.assertEqual(t.read(), 1)
        t.shift_right()
        self.assertEqual(t.read(), 0)
        t.write(2)
        t.shift_right()
        t.shift_left()
        self.assertEqual(t.read(), 2)
        t.shift_left()
        self.assertEqual(t.read(), 1)

