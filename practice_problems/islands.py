# Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
# A 1 represents land and 0 represents water,
# so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1


def number_of_islands(grid, num_cols, num_rows) -> int:
    num_found = 0 # the number of islands we've found
    # which islands have been seen at all
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if visited[row_idx][col_idx]:
                # has been seen, ignore
                pass
            else:
                explore(grid, row_idx, col_idx, visited)
                num_found += 1

    return num_found

def explore(grid, row_idx, col_idx, visited):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for (x_dir, y_dir) in directions:
        visited[row_idx + x_dir][col_idx + y_dir] = True
        if grid[row_idx + x_dir][col_idx + y_dir]:
            


grid = [[1, 0, 0, 0, 0,],
    [0, 0, 1, 1, 0,],
    [0, 1, 1, 0, 0,],
    [0, 0, 0, 0, 0,],
    [1, 1, 0, 0, 1,],
    [1, 1, 0, 0, 1,]]