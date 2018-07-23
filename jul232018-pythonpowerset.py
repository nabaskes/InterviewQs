# python function to express power sets

# Create a Python function that generates the power set given a set of values. For example, if you're given the following set:

# set = {1, 2, 3}

# Your python function should return the corresponding power set:

# power set = { {}, {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}, {1, 2, 3} }

# Upgrade to premium to receive in-depth solutions to each problem.


def power_set(lst):
    items = []
    for item in lst:
        items.append(lst.remove(item))
        items.extend(power_set(lst.remove(item)))
    return set(items)

# this is interesting ... is there a computationally good way to do this?
