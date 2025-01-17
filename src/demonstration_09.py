"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.

INPUT: letters --> array
OUTPUT: newDict --> dictionary listing the new uppercase letters
"""
def mapping(letters):
    newDict = {}
    # loop through the letters, convert the letter to uppercase based on index
    for ltr in letters:
        newDict[ltr] = ltr.upper()

    return newDict

print(mapping(["p", "s"]))
print(mapping(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"]))

