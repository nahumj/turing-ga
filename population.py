"""
The population class hold organisms and can advance by generation.
"""
from organism import Organism
from turing_rules import RuleGenerator
class Populaiton(object):
    def __init__(self, number_of_orgs, number_of_states, number_of_symbols):
        if number_of_orgs % 2 != 0 or number_of_orgs < 2:
            raise ValueError(
                    "Number of orgs must be an even number 2 or greater")
        self.rule_gen = RuleGenerator(number_of_states, number_of_symbols)

        number_of_inputs = number_of_states * number_of_symbols
        self.organisms = []
        for _ in range(number_of_orgs):
            rules = [self.rule_gen.make_rule()
                    for _ in range(number_of_inputs)]
            self.organisms.append(Organism(rules))


    def next(self):
        self.cull_half()
        self.duplicate_with_mutations()

    def cull_half(self):
        sorted_by_fitness = sorted(self.organisms, key=lambda org: org.fitness)
        self.organisms = sorted_by_fitness[:len(self.organisms)]

    def duplicate_with_mutations(self):
        new_orgs = [mutate(org) for org in self.organisms]
        self.organisms.extend(new_orgs)

def mutate(org):

