# Question 51 - Counting capital letters

# Using Python, write code that will read a file and return the number of capital letters. Once you have your initial piece of code, see if you can condense into a one-liner.

# Upgrade to premium to receive in-depth solutions to each problem.


def count_caps(text):
    return len([s for s in text if s.upper() == s])
