# The carshare dilemma

# We have selected a group of people to take a survey. 35% of the group like Uber, 20% like both Lyft and Uber, and 25% like neither Lyft nor Uber.

# Given this information, what percentage of the sample likes Lyft?

# Upgrade to premium to receive in-depth solutions to each problem.


'''
This is just a really simple set theory problem

We know that 25% of people like neither Lyft nor Uber.  So only 75% like
at least one of the car share.

Then, 35% of the entire sample like Uber, but only 20% of the sample like both.
So 15% of the entire sample must like only Uber.

This leaves 60% of the sample liking Lyft
'''

def get_last_choice(pct_a, pct_a_and_b, pct_neither):
    return 1 - pct_neither - (pct_a - pct_a_and_b)
