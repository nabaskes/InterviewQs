# Question 65 - Rolling 10 times

# Suppose a fair six-sided die is rolled 10 times. What is the probability that a 2 is rolled at least once? You may not need to explicitly solve this type of problem in an interview, but be prepared to share how you would structure an approach to a problem like this, using probability theory.

# Upgrade to premium to receive in-depth solutions to each problem.

'''

Each event is independent so we can just multiply the probabilities together.

On each roll, we have a 5/6 probability that we do not roll a two.  So, over ten rolls, we have a (5/6)^10 = 9765625/60466176 ~ 1/6 probability that we do not roll a two.  So we have a 1 - (5/6)^10 ~ 5/6 probability of rolling a two at least once

'''
