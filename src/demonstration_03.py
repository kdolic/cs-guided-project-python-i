"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12

INPUT: txt --> string
OUTPUT: txtToInt --> integer
"""
def string_int(txt):
    # convert string to integer value
    txtToInt = int(txt);

    return txtToInt;

print(string_int('6'));
