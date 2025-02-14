# This problem was asked by Twitter.

# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation.
# For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array.
# For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

from typing import List

def apply_permutation(permutation: List[int], l: List) -> List:
    return [l[permutation[i]] for i in range(len(permutation))]

assert(apply_permutation([2, 1, 0], ["a", "b", "c"]) == ["c", "b", "a"])
assert(apply_permutation([1, 2, 0], ["a", "b", "c"]) == ["b", "c", "a"])

