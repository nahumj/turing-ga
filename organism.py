"""
The Organism class represents the genetype and phenotype of a digital
organism.
"""
from turing_machine.system import System, DidNotHalt
from turing_machine.machine import Machine, Rule
from turing_machine.tape import Tape




class Organism(object):
    def __init__(self, rules):
        self.rules = rules

    def fitness(self):
        s = System(machine=Machine(self.rules))
        try:
            steps = s.iterate_until_halt(999)
        except DidNotHalt:
            steps = 0
        return steps
