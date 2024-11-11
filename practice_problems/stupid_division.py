# This question was asked by ContextLogic.

# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.

def stupid_division(a: int, b: int) -> int:
    quotient = 0
    while a >= b:
        a -= b
        quotient += 1
    return quotient

assert(stupid_division(4, 2) == 2)
assert(stupid_division(4, 3) == 1)
assert(stupid_division(100, 21) == 4)
