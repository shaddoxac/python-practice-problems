# This problem was asked by Triplebyte.

# You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

# You can generate random numbers between 0 and 1 uniformly.

from typing import List
import random

def generate(numbers: List[int], probs: List[float]) -> int:
    if len(numbers) != len(probs):
        raise RuntimeError("Must have same length!")
    
    random_num = random.random()

    cur_index = -1
    while random_num > 0.0:
        cur_index += 1
        random_num -= probs[cur_index]
    
    return numbers[cur_index]


