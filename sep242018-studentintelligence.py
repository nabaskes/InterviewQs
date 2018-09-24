# question 33 - Testing a claim around student intelligence

# Suppose you're consulting for a school district, and the head of the school district thinks the students have above average intelligence. A random sample of thirty students have a mean IQ score of 112. Is there sufficient evidence to support the head's claim?

# You can assume the mean IQ score across the population of all students (e.g. including students outside the head's school district) is 100, with a standard deviation of 15.

# Upgrade to premium to receive in-depth solutions to each problem.

'''

We probably just want 95% confidence intervals here.  First, we should take
the data from the 30 students and calculate the standard deviation.

Then, we take the standard deviation and divide it by the square root of the sample size sqrt(30) which is roughly 5.5.  Then we multiple this value by the confidence coefficient for 95%, which is 1.96.  This will give us the bounds on our 95% confidence interval.

Here, we want to be confident that the average IQ is above 100.  112 - 100 = 12, so we must have confidence intervals less than 12.  So

1.96 * (stdev / sqrt(30)) < 12

stdev < 12 * sqrt(30) / 1.96
therefore
stdev < 33.5

We'd need to calculate the standard deviation of this (relatively small) sample, but I expect it to be less than 33.5, considering that the value for all students is 15.

'''
