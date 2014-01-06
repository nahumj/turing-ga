"""
An implementation of the infinite tape needed by the turing computer.

It is implemented as two stacks that increase in depth as symbols are
written to them.

The blank symbol is represented by 'None'.
"""

class Tape(object):
    def __init__(self):
        self.left = []
        self.right = []
        self.head = None

    def head(self):
        return self.head

    def shift_left(self):
        self.right.append(self.head)
        if self.left:
            self.head = self.left.pop()
        else:
            self.head = None

    def shift_right(self):
        self.left.append(self.head)
        if self.right:
            self.head = self.right.pop()
        else:
            self.head = None

    def write(self, symbol):
        self.head = symbol

