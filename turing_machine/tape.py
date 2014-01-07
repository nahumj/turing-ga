"""
An implementation of the infinite tape needed by the turing computer.

It is implemented as two stacks that increase in depth as symbols are
written to them.

The blank symbol defaults to the integer 0.
"""
from itertools import dropwhile

class Tape(object):
    def __init__(self, blank_symbol=0):
        """
        The blank symbol is the tape's default symbol until something else
        is written.
        """
        self.left = []
        self.right = []
        self.blank_symbol = blank_symbol
        self.head = self.blank_symbol

    def read(self):
        """
        Returns the symbol underneath the head.
        """
        return self.head

    def shift_left(self):
        """
        Shifts the head to the left.
        """
        self.right.append(self.head)
        if self.left:
            self.head = self.left.pop()
        else:
            self.head = self.blank_symbol

    def shift_right(self):
        """
        Shifts the head to the right.
        """
        self.left.append(self.head)
        if self.right:
            self.head = self.right.pop()
        else:
            self.head = self.blank_symbol

    def write(self, symbol):
        """
        Writes (saves) the given symbol to the tape at the location
        of the head.
        """
        self.head = symbol

    def get_contents_and_index(self):
        """
        Returns a list containing the portion of the tape that has been
        written to and the index of the head. Excludes leftmost and rightmost
        blank symbols.

        The tape containing the head's location is always included in the tape.
        """
        is_blank_symbol = lambda x: x == self.blank_symbol
        contents = list(dropwhile(is_blank_symbol, self.left))
        head_index = len(contents)
        contents.append(self.head)
        contents.extend(reversed(list(dropwhile(is_blank_symbol, self.right))))
        return contents, head_index

