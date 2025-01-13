# This problem was asked by Uber.

# Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

# next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

# Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.



class TwoDimensionIterator:
    def __init__(self):
        self.arrays = []

    def next(self):
        for arr_idx in range(0, len(self.arrays)):
            if len(self.arrays[arr_idx]) > 0:
                ret = self.arrays[arr_idx][0]
                self.arrays[arr_idx] = self.arrays[arr_idx][1:]
                return ret
        raise Exception("No elements remain!")

    def has_next(self):
        for arr_idx in range(0, len(self.arrays)):
            if len(self.arrays[arr_idx]) > 0:
                return True
        return False
    
iter = TwoDimensionIterator()
iter.arrays = [[1, 2], [3], [], [4, 5, 6]]

assert(iter.has_next())
assert(iter.next() == 1)
assert(iter.next() == 2)
assert(iter.next() == 3)
assert(iter.next() == 4)
assert(iter.next() == 5)
assert(iter.next() == 6)
assert(not iter.has_next())
try:
    iter.next()
    assert(False)
except Exception:
    pass