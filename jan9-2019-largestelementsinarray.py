# Question 78 - Largest elements in an array

# Given an array with k distinct elements, write a function to return all elements that have at least two elements greater than themselves in the same array:

# For example, given the following array:
# array = [2,3,9,7,6]

# Your function should return:
# [2,3,6]

# Solution will be written in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.

'''
This should be O(n), the naive solution of sorting the array is bad unless
we also want a sorted array
'''


def get_all_but_largest_two(arr):
    largest = None
    second_largest = None
    for item in arr:
        if largest is not None and item > largest:
            second_largest = largest
            largest = item
        elif second_largest is not None and item > second_largest:
            second_largest = item
    return (item for item in arr if item < second_largest)
