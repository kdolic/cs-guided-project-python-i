"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []

INPUT: lst --> array 
OUTPUT: lst --> array (sorted)
"""
def sort_by_length(lst):
    # sort method to sort ascending order of input array values
    lst.sort();

    return lst;

print(sort_by_length(["a", "ccc", "dddd", "bb"]));