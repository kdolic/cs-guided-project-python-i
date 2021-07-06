"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22

INPUT: length, width --> integer, integer
OUTPUT: perimeter --> integer 
"""
def find_perimeter(length, width):
    # two sides of the rectangle length
    sumOfLength = length * 2;
    # two sides of the rectangle width
    sumOfWidth = width * 2;
    # sum of two sides
    rectanglePerimeter = sumOfLength + sumOfWidth;

    return rectanglePerimeter;

print(find_perimeter(20,10));