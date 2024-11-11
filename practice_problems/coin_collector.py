# This question was asked by Zillow.

# You are given a 2-d matrix where each cell represents number of coins in that cell.
# Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

# For example, in this matrix

# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


def get_max_coins(matrix) -> int:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    dynamic = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    dynamic[0][0] = matrix[0][0]
    dynamic[0][1] = matrix[0][0] + matrix[0][1]
    dynamic[1][0] = matrix[0][0] + matrix[1][0]

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            dynamic[i][j] = matrix[i][j] + max(dynamic[i-1][j], dynamic[i][j-1])

    return dynamic[-1][-1]



matrix = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1]
]
assert(get_max_coins(matrix) == 12)
