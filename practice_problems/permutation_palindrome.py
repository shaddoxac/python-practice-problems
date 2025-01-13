# This problem was asked by Amazon.

# Given a string, determine whether any permutation of it is a palindrome.

# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
from collections import defaultdict

def permutation_palindrome(s: str) -> bool:
    char_map = defaultdict(int)
    for c in s:
        char_map[c] += 1

    num_odd = 0
    for key in char_map.keys():
        if char_map[key] % 2 == 1:
            num_odd += 1

    return num_odd <= 1

assert(permutation_palindrome("carrace") == True)
assert(permutation_palindrome("racecar") == True)
assert(permutation_palindrome("daily") == False)
