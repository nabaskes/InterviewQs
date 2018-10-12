# Question 41 - Rolling dice to win...again

# Suppose you are playing a game where there are two fair six-sided dice, and every time you roll the dice and they add up to 9, you win $50. However, to roll the dice costs $20 to play. Is this a game you're willing to play?

# You should be able to attach an expected value to each dice roll using probability theory here.

# Upgrade to premium to receive in-depth solutions to each problem.

'''
This is an expected value problem.

For the first dice roll, 1 and 2 cannot add up to nine, so these are bad rolls
3, 4, 5, and 6 can.  However, each of them has exactly one possible second roll
to add to 9

3, 6
4, 5
5, 4
6, 3

So, there are 4 permutations that win.
There are 36 permutations total.

So, you have a 4/36 = 1/9 chance of winning

EV = $50 * 1/9 = $5.55

This is way less than $20, so I wouldn't recommend playing the game...
'''
