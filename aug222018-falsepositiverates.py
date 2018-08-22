#  Question 19 - New strain of flu

# You go to see the doctor about a cough you've had for a while. The doctor selects you at random to have a blood test for a new strain of flu, which for the purposes of this exercise we will say is currently suspected to affect 1 in 10,000 people in the US. The test is 99% accurate, in the sense that the probability of a false positive is 1%.

# The probability of a false negative is zero. You test positive. What is the new probability that you have this strain of flu?

# Upgrade to premium to receive in-depth solutions to each problem


'''
For the sample of 10,000, one person will have the disease and 1% of people
will falsely test positive.  .01 * 10000 = 100, so 101 people will test positive

But only 1 of those will actually have it, so you have a 1/101 chance of being
sick.  Good luck!
'''

def get_likelihood(false_positive_rate, incidence_rate):
    '''
    Gets the likelihood of you getting the disease
    '''
    return incidence_rate / (false_positive_rate + incidence_rate)
