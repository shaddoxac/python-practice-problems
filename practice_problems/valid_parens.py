# This problem was asked by Google.

# Given a string of parentheses,
# write a function to compute the minimum number of parentheses to be removed 
# to make the string valid (i.e. each open parenthesis is eventually closed).

# For example, given the string "()())()", you should return 1.
# Given the string ")(", you should return 2, since we must remove all of them.

def valid_parens(paren_str: str) -> int:
    num_removed = 0
    num_open = 0
    for char in paren_str:
        if char == '(':
            num_open += 1
        else: # next char is ')'
            if num_open:
                num_open -= 1
            else:
                num_removed += 1
        paren_str = paren_str[1:]

    return num_removed + num_open

assert(valid_parens("()())()") == 1)
assert(valid_parens(")(") == 2)

