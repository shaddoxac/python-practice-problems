# This problem was asked by Google.

# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
# For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

#   1
#  2 3
# 1 5 1
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, 
# eventually ending with an entry on the bottom row.
# For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

# Write a program that returns the weight of the maximum weight path.

from typing import List

def is_even(i) -> bool:
    return (i % 2) == 0

def get_highest_parent_val(scores: List[List[int]], i, j) -> int:
    # given a row, find the higher of the two parent values (if they exist)
    max_val = 0
    if i - 1 < 0:
        return max_val
    else:
        cur_row = scores[i-1]
        if len(cur_row) > j:
            max_val = max(max_val, cur_row[j])

        if len(cur_row) > j - 1 and j - 1 >= 0:
            max_val = max(max_val, cur_row[j-1])
    return max_val

def maximum_triangle_path(triangle: List[List[int]]) -> int:
    # prepopulate score array
    scores: List[List[int]] = []
    for i in range(len(triangle)):
        to_append = []
        for _ in range(len(triangle[i])):
            to_append.append(None)
        scores.append(to_append)

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            scores[i][j] = triangle[i][j] + get_highest_parent_val(scores, i, j)

    return max(scores[-1])


assert(maximum_triangle_path([[1], [2, 3], [1, 5, 1]]) == 9)
