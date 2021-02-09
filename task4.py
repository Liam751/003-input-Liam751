#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math

unit = input("What is the unit of mesument used? (example: cm, m, etc) ")
unit = unit.strip()
a = input("What is the length of one of the short sides? ")
a = float(a)
b = input("What is the length of the other short side? ")
b = float(b)

x = a**2 + b**2
x = math.sqrt(x)
x = str(x)
print("The length of the hypotenous is " + x + unit + ".")