# Question 62 - Subarray sums

# Suppose you're given an array of integers, and a number x. Write a function to find the smallest subarray with a sum greater than the given value. Given the array, the array's length n, and the number x your function should return:

#     The length of the smallest subarray that has a sum greater than x
#     The actual subarray that has a sum greater than x

# For example, given the following:
# array = [5,6,2,3,8]
# x = 12

# Your output should be:
# array length: 2
# array: [8,6] //note that [8, 5] would also be an acceptable answer, as it contains a length of 2 as well

# If the output is not possible, then you can return the length of the array + 1 (indicating that an additional element would be needed to satisfy the requirements). Solution will be written in python.

# Upgrade to premium to receive in-depth solutions to each problem.


def smallest_subarray_greater_than(arr, piv):
    'smallest subarray of arr greater than piv'
    for size in range(len(arr)):
        for i in range(len(arr) - size):
            if sum(arr[i:i+size]) > piv:
                return size, arr[i:i+size]
    return len(arr)+1, arr
# this question feels phrased poorly to me, it actually doesn't care about the order of the array.


def smallest_subset_greater_than(arr, piv):
    'this solves the actual problem they want'
    ordered_arr = sorted(arr)[::-1]
    # if we can mutate the original array we don't need O(n) extra space
    # if it's passed into a function we do
    for size in range(len(arr)):
        if sum(ordered_arr[:size]) > piv:
            return size, ordered_arr[:size]
    # ordering makes it so that we can check each size in only one step
    # this is still O(n^2) in time since we have to sum over elements,
    # 1 el for size 1, 2 els for size 2, etc.
    # but if len(arr) is large this collapses to roughly O(n) since we don't
    # need to sum over that much of the array.  In that case, total runtime is
    # O(nlogn), since we need to sort.
    return len(arr)+1, arr
