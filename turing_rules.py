"""
This module is responisble for generating valid turing machine rules and
mutating existing ones.
"""
from random import Random
from turing_machine.machine import Rule, Machine

class RuleGenerator(object):
    def __init__(self, number_of_states, number_of_symbols):
        if number_of_states < 2 or number_of_symbols < 2:
            raise ValueError(
                    "number of states and symbols must be greater than "
                    "or equal to 2.")
        self.number_of_states = number_of_states
        self.number_of_symbols = number_of_symbols
        self.rand_gen = Random()
        self.possible_rule_options = [
                list(range(self.number_of_states)),
                list(range(self.number_of_symbols)),
                list(range(self.number_of_symbols)),
                [True, False],
                list(range(self.number_of_states))]

    def make_rule(self):
        rule_args = [self.rand_gen.choice(o)
                for o in self.possible_rule_options]
        return Rule(*rule_args)

    def modify_rule(self, rule):
        field_to_modify = self.rand_gen.randrange(5)
        while True:
            new_option = self.rand_gen.choice(
                    self.possible_rule_options[field_to_modify])
            if new_option != rule[field_to_modify]:
                break
        return rule._replace(**{rule._fields[field_to_modify]:new_option})
