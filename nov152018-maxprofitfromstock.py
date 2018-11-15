# Question 54 - Sell, sell, sell!

# Suppose we are given an array of n integers which represent the value of some stock over time. Assuming you are allowed to buy the stock exactly once and sell the stock once, what is the maximum profit you can make? Can you write an algorithm using Python that takes in an array of values and returns the maximum profit?

# For example, if you are given the following array:

# 2, 7, 1, 8, 2, 8, 14, 25, 14, 0, 4, 5

# The maximum profit you can make is 24 because you would buy the stock when it's price is 1 and sell when it's 25. Note that we cannot make 25, because the stock is priced at 0 after it is priced at 25 (e.g you can't sell before you buy).

# Upgrade to premium to receive in-depth solutions to each problem.


def long_or_short_best_trade(stocks):
    '''note that this problem is easier if we can short sell,
    that is, if we can sell before we buy.
    This is a simple O(n) solution
    '''
    min_val = None
    max_val = None
    for stock in stocks:
        if min_val is None or stock < min_val:
            min_val = stock
        if max_val is None or stock > max_val:
            max_val = stock
    return max_val - min_val


def brute_force_best_trade(stocks):
    '''
    There is a simple brute force solution
    '''
    best_trade = 0
    for i in range(len(stocks)):
        stock = stocks[i]
        trade = max(stocks[i:]) - stock
        if trade > best_trade:
            best_trade = trade

    return best_trade


def best_trade(stocks):
    '''
    We can find a general O(n) solution if you note a property of a subsequence
    --> the only important properties of a subsequence are its lowest value,
    and its best trade.  So we step through the stock as folows
    For each stock we check if it's the lowest value so far.
    If it is we save it.
    We also check if its the highest value so far.  If it is, the new best
    trade would be it minus the lowest value,
    so we keep only this trade and continue.
    '''
    lowest_val = None
    highest_val = None
    for stock in stocks:
        if lowest_val is None or stock < lowest_val:
            lowest_val = stock
        if highest_val is None or stock > highest_val:
            highest_val = stock
            best_trade = (lowest_val, highest_val)
    return best_trade[1] - best_trade[0]
