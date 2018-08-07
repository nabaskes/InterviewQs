
# Question 12 - Finding the value closest to 0

# You are given a list of Q 1D points, return the value in Q that is the closest to value j.

# Example:

# Q = [1, -1, -5, 2, 4, -2, 1]

# j = 3

# The answer in this case 2.

# Solution will be provided in Python to premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


def closest_point_list(seq: list, q: float) -> float:
    if seq is None:
        return
    difference = abs(seq[0] - q)
    for s in seq:
        difference = abs(s - q) if abs(s - q) < difference else difference
    return difference
