# Question 50 - Python function to count tuple elements

# Suppose you are given a tuple containing ints and strings. Write a Python function to return the # of times a given element, n, appears in the tuple.

# For example, given the tuple below, where n=3, your function should return 4, since 3 appears 4 times in the tuple.

# my_tuple = 2, 'my_string', 4, 3, 3, 3, 2, 3

# Upgrade to premium to receive in-depth solutions to each problem.


def count_el(lst, el):
    return len(it for it in lst if it == el)
