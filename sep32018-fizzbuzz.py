# Question 24 - Oh foo-ie!

# Write a function that takes in an integer n, and prints out integers from 1 to n inclusive. If %3 == 0 then print "foo" in place of the integer, if %5 == 0 then print "ie" in place of the integer, and if both conditions are true then print "foo-ie" in place of the integer.

# Solution will be provided using Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


def fizzbuzz(n):
    return '\n'.join('fizz-buzz' if i % 15 == 0 else 'fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else i for i in range(1, n))
