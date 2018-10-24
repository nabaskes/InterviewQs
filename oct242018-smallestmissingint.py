# Question 46 - Smallest missing number in array

# Write a function that outputs the smallest missing number in a sorted array of n unique integers. The integers in the array range from 0 to m-1, where m > n.
# The function should be called SmallestMissingNumber and the 3 inputs are: the array, the "start value" of the array (e.g. 0), and the length of the array - 1, or "end value".

# Examples:
# Input: [0, 1, 3, 4, 8, 9], n = 5, m = 10
# Output: 2

# Input: [4, 7, 9, 11], n = 4, m = 12
# Output: 0

# Solution will be written using Python.

# Upgrade to premium to receive in-depth solutions to each problem.


def smallest_missing_number(arr, start, numels):
    for i, j in enumerate(range(start, start + numels)):
        if arr[i] != j:
            return j
