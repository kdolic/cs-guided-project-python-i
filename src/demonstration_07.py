"""
Challenge #7:
Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).
Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3

INPUT: lst --> array, n --> integer
OUTPUT: sortedLst --> integer or None
"""
def nth_smallest(lst, n):
  # sort method for lst input
    sortedLst = sorted(lst)
  # if the input number is less than or equal to the length of the lst array --> return smallest nth
    if n <= len(lst):
        return sortedLst[n - 1]
    else:
        return None

print(nth_smallest([7, 5, 3, 1], 1))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([7, 3, 5, 1], 2))