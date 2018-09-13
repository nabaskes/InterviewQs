# Question 28 - Winning the lottery!

# Suppose you're trying to figure out your chances of winning the lottery. The specific lottery you're interested in has 49 balls, each showing a single number. To win the jackpot you need to match 6 balls to win (note that order does not matter).

# What is the probability that you can win the jackpot, given you buy 1 ticket?

# What if you buy 3 lottery tickets?

'''
There isn't enough information to solve this problem.  If you got it in an interview, you'd neeed to get the range possible for each ball, and elaborate on what the matching condition would be.

If, say, six balls were drawn, each from 49 possibilities, without replacement...

There are 49 choose 6 possibilities, or (49!/(43! * 6!)) = 13,983,816

So for one ticket, your odds would be 1/13,989,816.

If you buy multiple tickets each one decreases the remaining search space.

For the first one, you have 13,989,815/13,989,816 chance of failure.
For the second one, you have 13,989,814/13,989,815 chance of failure.

And so one.  Multiply these together, and your success rate is
1 - (13,989,815*13,989,814*13,989,813)/(13,989,816*13,989,815*13,989,814) =
1 - (13,989,813)/(13,989,816) = 3/13,989,816.

Wow, buying three tickets makes you three times as likely to win...what are the odds???

'''
