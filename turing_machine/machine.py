"""
A repesentation of a Turing Machine.
Symbols are objects that can be written to the tape
States are objects denoting the machine memory-state

Rules are a tuple consisting of a input (current state and read symbol) and
output (symbol to write, direction to move (True = Right), and next state).

Start state defaults to the 'current state' of the first rule.
Halt state occurs when the current state and read symbol do not have an
associated rule.

Both states and symbols must be hashable objects.
"""
from collections import namedtuple

Rule = namedtuple('Rule', ['current_state', 'read_symbol',
    'write_symbol', 'shift_right', 'next_state'])

class Halt(Exception):
    pass

class Machine(object):
    def __init__(self, rules, start_state=None):
        self.rules = {(r.current_state, r.read_symbol) :
                (r.write_symbol, r.shift_right, r.next_state) for r in rules}
        if start_state is None:
            self.state = rules[0].current_state
        else:
            self.state = start_state

    def next(self, symbol):
        try:
            write_symbol, shift_right, next_state = self.rules[
                (self.state, symbol)]
        except KeyError:
            raise Halt()
        self.state = next_state
        return write_symbol, shift_right




