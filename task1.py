#! python3
# Ask the user for their name and their email address.
# (2 points)
#
# Inputs:
# name
# email
#
# Sample output:
# Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

name = input("What is your name human? ")
name = name.strip()
email = input("What is your email address? ")
email = email.strip()

print("Your name is " + name + ", and your email is " + email + ".")