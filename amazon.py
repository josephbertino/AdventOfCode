from collections import abc
import math

class IntIterator(abc):
    def has_next(self) -> bool:
        pass

    def next(self) -> int:
        pass

class MergeIterator(IntIterator):
    def __init__(self, iter_a, iter_b):
        """
        :param IntIterator iter_a:
        :param IntIterator iter_b:
        """
        self.iter_a = iter_a
        self.iter_b = iter_b
        self.val_a = None
        self.val_b = None

    def has_next(self):
        return self.val_a or self.val_b or self.iter_a.has_next() or self.iter_b.has_next()

    def next(self):
        if self.val_a is None and self.iter_a.has_next():
            self.val_a = self.iter_a.next()
        if self.val_b is None and self.iter_b.has_next():
            self.val_b = self.iter_b.next()

        retval = min(self.val_a or math.inf, self.val_b or math.inf)
        if retval == self.val_a:
            self.val_a = None
        else:
            self.val_b = None

        return retval