# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
#
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
#
# Do this in O(N) time.

from typing import List

def smart_max(matrix, i, j):
    ret = [
        (i - 1, j),
        (i - 1, j - 1),
        (i,     j - 1)
    ]
    max_val = matrix[i][j]
    for new_i, new_j in ret:
        if new_i >= 0 and new_i < len(matrix) and new_j >= 0 and new_j < len(matrix[new_i]):
            max_val = max(matrix[new_i][new_j], max_val)
    return max_val

def contiguous_sum(l: List[int]) -> int:
    num_records = len(l)
    matrix = [[0 for _ in range(num_records)] for _ in range(num_records)]

    for i in range(num_records):
        if l[i] > 0:
            matrix[i][i] = l[i]

    print(matrix)

    for i in range(num_records):
        for j in range(num_records):
            matrix[i][j] = smart_max(matrix, i, j)

    print(matrix)

    return matrix[-1][-1]

assert(contiguous_sum([34, -50, 42, 14, -5, 86]) == 137)
assert(contiguous_sum([-5, -1, -8, -9]) == 0)
