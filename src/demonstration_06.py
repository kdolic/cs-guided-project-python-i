"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False

INPUT: txt --> string
OUTPUT: True or False --> boolean
"""
def XO(txt):
    # method to lower case the input txt
    lowerText = txt.lower();
    # if the count of 'x' matches the count of 'o' --> True
    if lowerText.count("x") == lowerText.count("o"):
        return True
    elif lowerText.count("x") == 0 and lowerText.count("o") == 0:
        return True
    # otherwise --> False
    else:
        return False

print(XO("ooxx"))

