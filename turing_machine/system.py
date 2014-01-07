"""
The System class represents the Turing machine and its tape.

It allows the machine to be iterated until it halts.
"""
from machine import Halt
from tape import Tape

class DidNotHalt(Exception):
    """
    Raised if a machine did not halt in the alloted number of steps
    """
    pass

class System(object):
    def __init__(self, machine, tape=None):
        """
        Requires a machine instance, and defaults to the
        default tape is not supllied with one.
        """
        self.machine = machine
        if tape is None:
            self.tape = Tape()
        else:
            self.tape = tape
        self.steps = 0

    def next(self):
        """
        Allows the machine to proceed one step forward
        """
        self.steps += 1
        write_symbol, shift_right = self.machine.next(self.tape.read())
        self.tape.write(write_symbol)
        if shift_right:
            self.tape.shift_right()
        else:
            self.tape.shift_left()

    def iterate_until_halt(self, max_steps=None):
        """
        Iterates the machine until it halts. If max_step is supplied and
        reached before a halt occurs, DidNotHalt exception is raised.
        """
        while True:
            try:
                self.next()
            except Halt:
                return self.steps
            if max_steps is not None and self.steps >= max_steps:
                raise DidNotHalt()

    def get_state_tape_contents_and_head_index(self):
        tape_contents, head_index = self.tape.get_contents_and_index()
        return self.machine.state, tape_contents, head_index

