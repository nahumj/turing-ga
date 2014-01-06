"""
An implementation of the infinite tape needed by the turing computer.

It is implemented as two stacks that increase in depth as symbols are
written to them.

The blank symbol defaults to the integer 0.
"""
from itertools import dropwhile

class Tape(object):
    def __init__(self, blank_symbol=0):
        self.left = []
        self.right = []
        self.blank_symbol = blank_symbol
        self.head = self.blank_symbol

    def read(self):
        return self.head

    def shift_left(self):
        self.right.append(self.head)
        if self.left:
            self.head = self.left.pop()
        else:
            self.head = self.blank_symbol

    def shift_right(self):
        self.left.append(self.head)
        if self.right:
            self.head = self.right.pop()
        else:
            self.head = self.blank_symbol

    def write(self, symbol):
        self.head = symbol

    def get_state(self):
        is_blank_symbol = lambda x: x == self.blank_symbol
        contents = list(dropwhile(is_blank_symbol, self.left))
        head_index = len(contents)
        contents.append(self.head)
        contents.extend(reversed(list(dropwhile(is_blank_symbol, self.right))))
        return contents, head_index

