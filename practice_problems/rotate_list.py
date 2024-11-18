# This problem was asked by Facebook.

# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list. How many swap or move operations do you need?

from typing import List


def rotate_list_left(l: List, k: int, verbose: bool = False) -> List:
    num_elems = len(l)
    # start by assuming k is smaller than l
    if k >= num_elems:
        # if it is larger, we only need the remainder since shifting num_elems is the same as doing nothing
        k = k % num_elems

    if k == 0:  # no rotation to perform
        return l

    to_reassign = l[:k]  # starts as first k elements
    cur_reassign_index = k - 1

    for i in range(num_elems):
        r_index = (
            num_elems - 1 - i
        ) % num_elems  # start at end of list, iterate back to beginning
        if verbose:
            print(f"Setting l[{r_index}] to {to_reassign[cur_reassign_index]}")
        tmp_value = l[r_index]  # value we will reassign later
        l[r_index] = to_reassign[
            cur_reassign_index
        ]  # set list element as current 'swap' element

        to_reassign[
            cur_reassign_index
        ] = tmp_value  # we will set this value in the list when we get back to it
        if verbose:
            print(f"Reassign[{cur_reassign_index}] to {tmp_value}")
        cur_reassign_index = cur_reassign_index - 1
        if cur_reassign_index < 0:  # make sure we keep cur_reassign_index in bounds
            cur_reassign_index = k - 1

    return l


# i made this function before realizing it was asking to shift LEFT not right
# ah well, nice to have
def rotate_list_right(l: List, k: int, verbose: bool = False) -> List:
    num_elems = len(l)
    # start by assuming k is smaller than l
    if k >= num_elems:
        # if it is larger, we only need the remainder since shifting num_elems is the same as doing nothing
        k = k % num_elems

    if k == 0:  # no rotation to perform
        return l

    to_reassign = l[:k]
    cur_reassign_index = 0

    for i in range(num_elems):
        l_index = (i + k) % num_elems  # current index to swap TO
        if verbose:
            print(f"Setting l[{l_index}] to {to_reassign[cur_reassign_index]}")
        tmp_value = l[l_index]  # value we will reassign later
        l[l_index] = to_reassign[cur_reassign_index]

        to_reassign[cur_reassign_index] = tmp_value
        if verbose:
            print(f"Reassign[{cur_reassign_index}] to {tmp_value}")
        cur_reassign_index = (cur_reassign_index + 1) % k

    return l


assert rotate_list_left([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
assert rotate_list_left([1, 2, 3, 4, 5, 6], 8) == [3, 4, 5, 6, 1, 2]

assert rotate_list_right([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
assert rotate_list_right([1, 2, 3, 4, 5, 6], 8) == [5, 6, 1, 2, 3, 4]


# update - the answer provided by Daily Coding Problem isn't as efficient as what i did, but it is interesting
def rotate_DCP(lst, k) -> List:
    reverse(lst, 0, k - 1)
    reverse(lst, k, len(lst) - 1)
    reverse(lst, 0, len(lst) - 1)
    return lst


def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


assert rotate_DCP([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
# it doesn't properly handle rotations beyond len(lst) either
# assert(rotate_DCP([1, 2, 3, 4, 5, 6], 8) == [3, 4, 5, 6, 1, 2])
