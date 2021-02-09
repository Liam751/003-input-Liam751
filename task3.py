#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("The equation format is ax + b = c.")
print("\n")
a = input("What is the value of a? ")
a = float(a)
b = input("What is the value of b? ")
b = float(b)
c = input("What is the value of c? ")
c = float(c)
print("\n")

y = c - b
x = y / a
x = str(x)

print("The value of x is " + x + ".")