# This problem was asked by Yelp.

# Given a mapping of digits to letters (as in a phone number),
# and a digit string, return all possible letters the number could represent.
# You can assume each valid number in the mapping is a single digit.

# For example if {"2": ["a", "b", "c"], 3: ["d", "e", "f"], …} then "23" should return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

from typing import List

mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r"],
    "8": ["s", "t", "u"],
    "9": ["v", "w", "x"],
    "0": ["y", "z"] 
}


def all_possible_vals(num_str: str) -> List[str]:
    all_results = []
    for num_char in num_str:
        if not all_results:
            all_results = mapping[num_char]
        else:
            tmp_all_results = all_results
            all_results = []
            for res in tmp_all_results:
                for possible_char in mapping[num_char]:
                    all_results.append(res + possible_char)
    return all_results

assert(all_possible_vals("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
