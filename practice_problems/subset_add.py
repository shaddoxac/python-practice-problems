# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
# If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

from typing import Dict, List, Optional

def subset_add_helper(l: List, index: int, k: int, solved_cases: Dict) -> Optional[List]:
    if len(l) <= index:
        return None
    if (index, k) in solved_cases:
        return solved_cases[(index, k)]
    
    cur_val = l[index]
    if cur_val == k:
        solved_cases[(index, k)] = [cur_val]
        return solved_cases[(index, k)]
    
    if cur_val < k:
        rest_solution = subset_add_helper(l, index + 1, k-cur_val, solved_cases)
        if rest_solution:
            solved_cases[(index, k)] = [cur_val] + rest_solution
            return solved_cases[(index, k)]
    
    return subset_add_helper(l, index=index + 1, k=k, solved_cases=solved_cases)

def subset_add(l: List, k: int) -> Optional[List]:
    return subset_add_helper(l, index=0, k=k, solved_cases={})
    

assert(subset_add([12, 1, 61, 5, 9, 2], k=24).sort() == [12, 9, 2, 1].sort())
assert(subset_add([12], k=13) == None)
assert(subset_add([12, 1, 61, 5, 9, 2], k=14).sort() == [12, 2].sort())
