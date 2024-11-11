# We can determine how "out of order" an array A is by counting the number of inversions it has.
# Two elements A[i] and A[i] form an inversion if A[i] > A[i] but i < i.
# That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions.
# The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
# The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

from typing import List

def inversions(l: List) -> int:
    num_inversions = 0
    if len(l) <= 1:
        return num_inversions
    
    for i in range(len(l)-1):
        while i >= 0 and l[i] > l[i+1]:
            tmp = l[i]
            l[i] = l[i+1]
            l[i+1] = tmp
            num_inversions += 1
            i -= 1
    
    return num_inversions

def merge(l: List, left, mid, right) -> int:
    print(f"merge l:{l}, left={left}, mid={mid}, right={right}")
    num_inversions = 0    
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = l[left + i]
    for j in range(n2):
        R[j] = l[mid + 1 + j]

    i = 0 # left index
    j = 0 # right index
    k = left # index of new data

    while i < n1 and j < n2:
        print(f"Comparing {L[i]} and {R[j]}")
        if L[i] <= R[j]:
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
            print(f"Adding inversion!")
            num_inversions += 1
        k += 1

    # add rest of L
    while i < n1:
        print(R)
        print(f"R is empty ({n2}, {len(R)})!!! adding inversion")
        print(L[i:])
        l[k] = L[i]
        i += 1
        k += 1
        num_inversions += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        l[k] = R[j]
        j += 1
        k += 1
    
    return num_inversions
    
def merge_sort(l: List, left, right) -> int:
    sum = 0
    if left < right:
        mid = (left + right) // 2
        sum += merge_sort(l, left, mid)
        sum += merge_sort(l, mid+1, right)
        sum += merge(l, left, mid, right)
    return sum


def inversions2(l: List) -> int:
    left = 0
    right = len(l) - 1
    ret = merge_sort(l, left, right)
    print(l)
    print(ret)
    return ret


assert(inversions2([2, 4, 1, 3, 5]) == 3)
assert(inversions2([5, 4, 3, 2, 1]) == 10)
