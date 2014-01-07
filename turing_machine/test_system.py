from unittest import TestCase
from system import System, DidNotHalt
from machine import Rule, Halt, Machine
from tape import Tape

class TestSystem(TestCase):
    def test_init_default(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        m = Machine(rules)
        s = System(m)
        self.assertEqual(s.tape.read(), 0)

    def test_init(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        m = Machine(rules)
        t = Tape()
        s = System(m, t)
        self.assertEqual(s.steps, 0)

    def test_next(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        m = Machine(rules)
        t = Tape()
        s = System(m, t)
        s.next()
        self.assertEqual(s.steps, 1)

    def test_get_state_tape_contents_and_index(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        m = Machine(rules)
        t = Tape()
        s = System(m, t)
        s.next()
        state, contents, index = s.get_state_tape_contents_and_head_index()
        self.assertEqual(state, "B")
        self.assertEqual(contents, [1, 0])
        self.assertEqual(index, 1)

    def test_iterate_until_halt(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        m = Machine(rules)
        t = Tape()
        s = System(m, t)
        steps = s.iterate_until_halt()
        self.assertEqual(steps, 14)
        state, contents, index = s.get_state_tape_contents_and_head_index()
        self.assertEqual(state, "HALT")
        self.assertEqual(contents, 6 * [1])
        self.assertEqual(index, 4)

    def test_iterate_until_halt_max(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        m = Machine(rules)
        t = Tape()
        s = System(m, t)
        with self.assertRaises(DidNotHalt):
            s.iterate_until_halt(max_steps=10)
        self.assertNotEqual(s.machine.state, "HALT")
