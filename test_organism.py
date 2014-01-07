from unittest import TestCase
from organism import Organism
from turing_machine.system import System, DidNotHalt
from turing_machine.machine import Rule, Machine

class TestOrganism(TestCase):
    def test_init(self):
        o = Organism([])

    def test_fitness(self):
        rules = [
                Rule("A", 0, 1, True, "B"),
                Rule("B", 0, 1, False, "A"),
                Rule("C", 0, 1, False, "B"),
                Rule("A", 1, 1, False, "C"),
                Rule("B", 1, 1, True, "B"),
                Rule("C", 1, 1, True, "HALT"),
                ]
        o = Organism(rules)
        self.assertEqual(o.fitness(), 14)

    def test_fitness_not_halt(self):
        rules = [
                Rule("A", 0, 1, True, "A"),
                Rule("A", 1, 1, True, "A"),
                ]
        o = Organism(rules)
        self.assertEqual(o.fitness(), 0)
