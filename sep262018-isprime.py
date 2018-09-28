# Question 34 - Identifying prime numbers with Python

# A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. Given a single #, n, write a function using Python to return whether or not the # is prime. Additionally, if the inputted # is prime, save it into an array, a.

# Solution will be provided for premium users using Python.

# Upgrade to premium to receive in-depth solutions to each problem.


def isprimep(n):
    'determines whether n is prime'
    if n % 2 == 0:
        return False

    sqrn = int(float(n)**0.5)
    for k in range(3, sqrn + 2, 2):
        if n % k == 0:
            return False
    return True


# cleaner >>>
def isprimep(n):
    'determins whether n is prime'
    return n % 2 != 0 and all(n % k != 0
                              for k in range(3, int(float(n)**0.5) + 2, 2))
