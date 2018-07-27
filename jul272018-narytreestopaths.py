# Question 8 - Python function to traverse a binary tree path

# Question: For a given binary tree, write a function to return all root-to-leaf paths.

# We'll use the tree below to walk through how your code should work. "A" is the root, and "E" would be considered the leaf in the path A-> B -> E.

# The expectation for your function is to return all root to leaf combinations.

# The output of your code, given the tree below, would be: ["A -> B -> E", "A -> B -> D", "A-> C"]


#            A

#          /   \


#         B     C

#       /   \

#      E     D

# Solution will be provided in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.

import functools

def tree_to_paths(root, cur_path=None):
    if root is None:
        return cur_path
    if cur_path is None:
        cur_path = ''
    cur_path += root.name

    return functools.reduce(
        lambda x, y: x.extend(y),
        (tree_to_paths(child, cur_path) for child in root.children))
