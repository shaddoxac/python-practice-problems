# This problem was asked by Jane Street.

# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# You can assume the given expression is always valid.

from typing import List

def solve_polish_notation_math(args: List) -> int:
    stack = []
    for arg in args:
        if arg == "+":
            stack.append(stack.pop() + stack.pop())
        elif arg == "-":
            stack.append(stack.pop() - stack.pop())
        elif arg == "*":
            stack.append(stack.pop() * stack.pop())
        elif arg == "/":
            stack.append(stack.pop() / stack.pop())
        else:
            stack.append(arg)
    return stack.pop()

assert(solve_polish_notation_math([5, 3, '+']) == 8)
assert(solve_polish_notation_math([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5)
