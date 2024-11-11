# This problem was asked by Dropbox.

# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
# The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

# Implement an efficient sudoku solver.

from typing import List, Set

ALL_POSSIBLE_SOLUTIONS = Set(1,2,3,4,5,6,7,8,9)

def solve_sudoku(grid):
    possible_solutions: List[List[Set]] = [[ALL_POSSIBLE_SOLUTIONS for _ in range(9)] for _ in range(9)]

    # iterate over every row
    for i in range(9):
        row = Set(rec for rec in grid[i] if rec)
        for j in range(9):
            possible_solutions[i][j] -= row

    # iterate over every column
    for j in range(9):
        row = Set()
        for i in range(9):
            if grid[i][j]:
                row.add(grid[i][j])
        for i in range(9):
            possible_solutions[i][j] -= row

    # iterate over every square
    for square_i in range(3):
        for square_j in range(3):
            row = Set()
            for i in range(3):
                for j in range(3):
                    if grid[square_i*3 + i][square_j*3 + j]:
                        row.add(grid[square_i*3 + i][square_j*3 + j])
            for i in range(3):
                for j in range(3):
                    possible_solutions[square_i*3 + i][square_j*3 + j]  -= row

    # possible solutions is done
                    
    # from here, we need to find possible_solutions with ONE option
    (x, y) = find_solution(grid, possible_solutions)
    while x != -1 and y != -1:
        set_val = possible_solutions[x][y].iterator().next()
        grid[x][y] = set_val
        for j in range(9):
            grid[x][j] -= set_val
        for i in range(9):
            grid[i][j] -= set_val
        for i in range(3):
            for j in range(3):
                grid[(x%3)*3+i][(y%3)*3+j] -= set_val # TODO check this
        
        
    

def find_solution(matrix, possible_solutions):
    for i in range(9):
        for j in range(9):
            if not matrix[i][j] and len(possible_solutions[i][j]) == 1:
                return (i, j)
    return (-1, -1)


# j  012345678
# i 
# 0  003020600
# 1  900305001
# 2  001806400
# 3  008102900
# 4  700000008
# 5  006708200
# 6  002609500
# 7  800203009
# 8  005010300
