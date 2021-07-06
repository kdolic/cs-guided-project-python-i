"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120

INPUT: minutes --> integer
OUTPUT: seconds --> integer
"""
def convert(minutes):
    # number of seconds in a minute
    oneMinInSeconds = 60;
    # converting minute to seconds by taking input of minutes times the number of seconds in a minute
    minToSec = minutes * oneMinInSeconds;

    return minToSec;

print(convert(5));

