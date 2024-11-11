# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

from typing import List

is_perfect_list: List[bool] = []
perfect_list: List[int] = []

def perfect_n(n: int) -> int:
    n = n - 1  # off by 1
    if len(perfect_list) > n:
        return perfect_list[n]
    
    i = len(is_perfect_list) - 1

    while True:
        is_perfect_list.append(is_perfect(i))
        if is_perfect_list[-1]:
            perfect_list.append(i)
            if len(perfect_list) > n:
                return perfect_list[n]
        i += 1



def is_perfect(i: int) -> bool:
    total = 0
    while i > 0:
        total += i % 10
        i = int(i / 10)
    return total == 10


assert(perfect_n(1) == 19)
assert(perfect_n(2) == 28)
