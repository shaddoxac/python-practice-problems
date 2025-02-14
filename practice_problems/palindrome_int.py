# This problem was asked by Palantir.

# Write a program that checks whether an integer is a palindrome. 
# For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
# Do not convert the integer into a string.


def is_palindrome(i: int) -> bool:
    # stack contains each individual digit in reverse order
    stack = []
    while i > 0:
        stack.append(i % 10)
        i = int(i / 10)

    # second half is the collection of characters in the second half
    second_half = []
    num_elems_to_compare = int(len(stack) / 2)
    for _ in range(num_elems_to_compare):
        second_half.append(stack.pop())

    # if the first half is equal to the reversed second half, then it is a palindrome
    return stack[:num_elems_to_compare] == second_half

assert(is_palindrome(121))
assert(is_palindrome(888))
assert(not is_palindrome(678))
assert(is_palindrome(12345678987654321))
assert(is_palindrome(1234567887654321))
