# This problem was asked by Amazon.

# Implement a bit array.

# A bit array is a space efficient array that holds a value of 1 or 0 at each index.

# init(size): initialize the array with size
# set(i, val): updates index at i with val where val is either 1 or 0.
# get(i): gets the value at index i.

from typing import Tuple

NUM_BITS_IN_INT = 32

class BitArray:
    def __init__(self, size: int):
        self.size = size
        self.array_vals = [0 for _ in range(int(size / NUM_BITS_IN_INT) + 1)]

    def set(self, i: int, val: int):
        if val > 1:
            raise Exception("Invalid val passed to set!")
        
        (bit_index, array_index) = self.get_indexes_from_raw_index(i)
        self.array_vals[array_index] |= val << bit_index

    def get(self, i: int) -> int:
        (bit_index, array_index) = self.get_indexes_from_raw_index(i)
        return 1 if self.array_vals[array_index] & (1 << bit_index) > 0 else 0


    # for a given i, return the bit_index and array_index corresponding to this entry
    def get_indexes_from_raw_index(self, i: int) -> Tuple[int, int]:
        bit_index = i % NUM_BITS_IN_INT
        array_index = int(i / NUM_BITS_IN_INT)
        return (bit_index, array_index)
    

arr = BitArray(64)
arr.set(0, 1)
assert arr.get(0) == 1
assert arr.get(1) == 0
arr.set(0, 0)
assert arr.get(1) == 0

arr.set(38, 1)
assert arr.get(38) == 1
