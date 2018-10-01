# Question 36 - Rolling to win!

# Suppose you are playing a game with a fair die (e.g. no bias for any one side), and your expected payout based on the # you roll is shown the table below. If you have to pay $1 to play, is it worth the cost to play?
# Roll 	Payout
# 6 	$4
# 5 	$2
# 4 	$1
# 3 	$0
# 2 	$0
# 1 	$0

# Upgrade to premium to receive in-depth solutions to each problem.

'''

Generally, we just need to calculate the expected value.  This takes the form of an integral of the result function over the probability space.

For a discrete space, this is

(1/6) Σ_i V_i

Since each step has the same likelihood, its just

sum(Payout) / len(Roll) = 7/6

This is greater than 1 so you're likely to prevail.

That said, this has a fifty percent chance of you losing all your money.  So, if you do it a large number of times you'll very likely profit, but for a small number of times you very likely would not

'''
