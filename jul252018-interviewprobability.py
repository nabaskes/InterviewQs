# Probability of passing through interview stages

# Question: Give the information below, if you had a good first interview, what is the probability you will receive a second interview?

#     50% of all people who received a first interview received a second interview
#     95% of people that received a second interview had a good first interview
#     75% of people that did not receive a second interview had a good first interview

# Upgrade to premium to receive in-depth solutions to each problem.

'''
Given:

P(2|1) = .5
P(G|2) = .95
P(G|~2) = .75

We know that:
P(~G|2) = .05
P(~2|1) = .5
P(~G|~2) = .25

Given 50% of people had a second interview and 95% of them had a good interview:
Then 47.5% of the total had a good first and a second
2.5% had a bad first and a second

Given 50% of people didn't have a second interview and 75% of them had a good
interview:
Then 37.5% of the total had a good interview and didn't get a second
12.5% had a bad first and didn't get a second

So 15% of people had a bad first and 85% had a good first.

Then since 47.5%/85% of people with good firsts got a second

So if you had a good first you have a 55% of getting a second

This is a lot better than 16.7% chance if you had a bad first!!!
'''
