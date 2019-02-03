# Question 86 - Alternative array sorting

# Given an array of integers, print the array in alternating min/max order. The first element should be the first maximum, second element should be the first minimum, third element should be second maximum, etc.

# For example, given the following array:

# arr[] = [10, 2, 11, 3, 7, 4, 1]

# Your function should return:

# 11, 1, 10, 2, 7, 3, 4

# Solution will be written in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


def folded_sort_array(arr):
    darr = sorted(arr)[::-1]
    steps = len(arr) // 2

    if len(arr) % 2 == 1:
        arr[-1] = darr[steps]

    for i in range(steps):
        arr[2 * i] = darr[i]
        arr[2 * i + 1] = darr[-1-i]
    return arr

# is there a good way to do this in situ?


if __name__ == "__main__":
    its = list(range(10))
    print(folded_sort_array(its))
    arr = [10, 2, 11, 3, 7, 4, 1]
    print(folded_sort_array(arr))
