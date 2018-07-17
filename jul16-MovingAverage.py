# Calculating a moving average using Python

# You are given a list of numbers J and a single number p.
# Write a function to return the minimum and maximum averages of the sequences of p numbers in J.

# Example:

# J = [4, 4, 4, 9, 10, 11, 12]

# p = 3

# The sequences will be:

# (4,4,4)

# (4,4,9)

# (4,9,10)

# (9,10,11)

# (10,11,12)

# Here the minimum average will be 4 and the maximum average will be 11, which corresponds to the first and last sequences. Solution will be provided in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.

def avg_span(lst, p):
    curr_avg = mean(last[:p])
    seqmin = curr_avg
    seqmax = curr_avg
    lnum = lst[0]
    for outn, num in zip(lst[:-p], last[p:]):
          curr_avg += float(num/p) - float(outn/p)
          seqmax = max(curr_avg, seqmax)
          seqmin = min(curr_avg, seqmax)
    return seqmax, seqmin
