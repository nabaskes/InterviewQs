# Question 66 - Matrix frequencies

# Given a matrix of order m*n then the task is to find the frequency of even and odd numbers in matrix.

# For example, given the following inputs:
# m = 2, n = 3
# [[ 9, 11, 3 ],
# [ 4, 12, 2 ]]

# Your function should return the following output:
# Frequency of odd #: 3
# Frequency of even #: 3

# Upgrade to premium to receive in-depth solutions to each problem.


def even_odd_count(mat):
    even = 0
    odd = 0
    for row in mat:
        for item in row:
            if item % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd
