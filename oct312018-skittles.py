# Question 49 - Skittles from a bag

# Suppose a bag contains 40 skittles: 16 yellow, 14 red, and 10 orange. You draw 3 skittles at random (without replacement) from the bag. What is the probability that you get 2 skittles of one color and another skittle of a different color?

# Upgrade to premium to receive in-depth solutions to each problem.

'''
There are 40C3 = 401!/(37!*3!) = (40*39*38)/(3*2) = 9880 possible combinations
Of these, 16*14*10 = 2240 have three different colors of skittle
Also, 10C3 + 16C3 + 14C3 = (10*9*8)/(3*2) + (16*15*14)/6 + (14*13*12)/6 = 120 + 560 + 364 = 1044 have one color of skittle.

As such, (9880 - 2240 - 1044)/9880 = 6596/9880 = 66.76% ~ 2/3 chance of getting two of one colors and one of another
'''x
