# This problem was asked by Facebook.

# Given three 32-bit integers x, y, and b, 
# return x if b is 1 and y if b is 0, 
# using only mathematical or bit operations. 
# You can assume b can only be 1 or 0.

def bit_math(x, y, b):
    return (x * b) + (y * (b ^ 1))

assert(bit_math(3, 4, 1) == 3)
assert(bit_math(3, 4, 0) == 4)
