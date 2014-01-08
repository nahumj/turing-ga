from unittest import TestCase
from turing_rules import RuleGenerator
from turing_machine.machine import Rule

class TestRuleGenerator(TestCase):
    def test_init(self):
        r_gen = RuleGenerator(2, 3)
        self.assertEqual(r_gen.number_of_states, 2)
        self.assertEqual(r_gen.number_of_symbols, 3)

    def test_init_error(self):
        with self.assertRaises(ValueError):
            RuleGenerator(1, 3)
        with self.assertRaises(ValueError):
            RuleGenerator(3, 1)

    def test_make_rule(self):
        r_gen = RuleGenerator(3, 2)
        rule = r_gen.make_rule()
        self.assertIn(rule[0], list(range(3)))
        self.assertIn(rule[1], list(range(2)))
        self.assertIn(rule[2], list(range(2)))
        self.assertIn(rule[3], [True, False])
        self.assertIn(rule[4], list(range(3)))

    def test_modify_rule(self):
        r_gen = RuleGenerator(3, 2)
        rule = Rule(0, 1, 1, True, 2)
        rule2 = r_gen.modify_rule(rule)
        self.assertNotEqual(rule, rule2)


