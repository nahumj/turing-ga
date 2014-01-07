from unittest import TestCase
from machine import Rule, Halt, Machine

class Test_Machine(TestCase):
    def test_create_rule(self):
        r = Rule(current_state='A', read_symbol=0, write_symbol=1,
                shift_right=True, next_state="B")
        r2 = Rule("A", 0, 1, True, "B")
        self.assertEqual(r, r2)

    def test_machine_init(self):
        r1 = Rule("A", 0, 1, True, "B")
        r2 = Rule("A", 1, 1, True, "A")
        r3 = Rule("B", 0, 1, False, "A")
        m = Machine(rules=[r1, r2, r3])
        self.assertEqual(m.state, "A")

    def test_machine_next(self):
        r1 = Rule("A", 0, 1, True, "B")
        r2 = Rule("A", 1, 1, True, "A")
        r3 = Rule("B", 0, 0, False, "B")
        m = Machine(rules=[r1, r2, r3])
        write_symbol, shift_right = m.next(1)
        self.assertEqual(m.state, "A")
        self.assertEqual(write_symbol, 1)
        self.assertEqual(shift_right, True)

        write_symbol, shift_right = m.next(0)
        self.assertEqual(m.state, "B")
        self.assertEqual(write_symbol, 1)
        self.assertEqual(shift_right, True)

        write_symbol, shift_right = m.next(0)
        self.assertEqual(m.state, "B")
        self.assertEqual(write_symbol, 0)
        self.assertEqual(shift_right, False)

        with self.assertRaises(Halt):
            write_symbol, shift_right = m.next(1)
