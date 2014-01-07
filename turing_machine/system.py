"""
The System class represents the Turing machine and its tape.

It allows the machine to be iterated until it halts.
"""
from machine import Halt

class System(object):
    def __init__(self, machine, tape):
        self.machine = machine
        self.tape = tape
        self.steps = 0

    def next(self):
        self.steps += 1
        write_symbol, shift_right = self.machine.next(self.tape.read())
        self.tape.write(write_symbol)
        if shift_right:
            self.tape.shift_right()
        else:
            self.tape.shift_left()

    def iterate_until_halt(self, max_steps=None):
        while self.steps != max_steps:
            try:
                self.next()
            except Halt:
                break
        return self.steps

    def get_state_tape_contents_and_head_index(self):
        tape_contents, head_index = self.tape.get_contents_and_index()
        return self.machine.state, tape_contents, head_index

