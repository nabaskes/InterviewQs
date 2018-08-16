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


def point_in_max_intervals(point, intervals):
    intervals = sorted(intervals, key=lambda x: x[1])

    max_num_intervals = 0

    for i in range(min(ivl[0] for ivl in intervals), intervals[-1][1]):
        num_intervals = 0

        for count, interval in enumerate(intervals):
            if interval[0] <= i and interval[1] >= i:
                num_intervals += 1
            if interval[1] < i:
                if count != 0:
                    intervals = intervals[count - 1:]
                break
        if i == point:
            point_num_intervals = num_intervals

        if num_intervals > max_num_intervals:
            max_num_intervals = num_intervals

    '''This is still O(n^2) but it should be a slightly better one
    Basically this should run in less time for sufficiently large n,
    whenever the n^2 term that is subtracted by iterating over less stuff
    is greater than the additional nlogn term.

    On average, this should take about half as much space, as we remove from
    the list any intervals that occur before it.  Additionally, since we only
    run through intervals that could possibly work, the n^2 term should be
    a linear factor faster'''
    return point_num_intervals >= max_num_intervals


class IntervalMap:
    def __init__(self, intervals):
        self.min = min(interval[0] for interval in intervals)
        self.max = max(interval[1] for interval in intervals)

        self.max_num_intervals = 0
        self.numbers_in_max = set

        for i in range(self.min, self.max):
            num_intervals = 0
            for count, interval in enumerate(intervals):
                if interval[0] <= i and interval[1] >= i:
                    num_intervals += 1
                if interval[1] < i:
                    if count != 0:
                        intervals = intervals[count - 1:]
                    break

            if num_intervals >= self.max_num_intervals:
                if num_intervals > self.max_num_intervals:
                    self.max_num_intervals = num_intervals
                    self.numbers_in_max = set(i)
                else:
                    self.numbers_in_max.add(i)

    def point_in_max_intervals(self, point):
        return point in self.numbers_in_max

    '''This is still n^2 might be amortized lower.

    Let n be the number of intervals, and N be the number of points we test.

    Then this is O(n^2).  If n >> N, then this is O(n^2).  If N >> n, then this
    is O(N)'''
