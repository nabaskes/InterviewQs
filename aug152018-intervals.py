# Question 16 - Points within an interval

# You are given j integer intervals in the format [a,b] (e.g. if j = 2, would get list of 2 intervals [a,b], [c,d] where a, b, c, and d are integer #s). The absolute value of the coordinates is bound by a value M.

# Build a Python function that determines whether or not a given point belongs to the maximum number of intervals provided.

# Upgrade to premium to receive in-depth solutions to each problem.


def get_intervals(point, intervals):
    return (interval for interval in intervals if point <= interval[1] and point >= interval[0])

def point_in_max_intervalsp(point, intervals):
    max_num_intervals = 0
    max_val = 0
    for i in range(min(interval[0] for interval in intervals),
                   max(interval[1] for interval in intervals)):
        num_intervals = len(get_intervals(i, intervals))
        if num_intervals > max_num_intervals:
            max_val = i
            max_num_intervals = num_intervals
    return len(get_intervals(point, intervals)) == max_num_intervals

# This is basically a naive O(n^2) solution.  Is there a better way?
