# Question 45 - Defective gaskets

# Suppose you're working in a parts manufacturing plant, and you're running quality analysis on the gasket production line. Gaskets produced by your company will be defective 1% of the time, and are distributed in packs of 20.

# Your company has a policy where if 1 or more of the 20 gaskets in a given pack is defective, they will replace the entire package. What proportion of packages does the company need to replace?

# If you're struggling with where to start here, consider that this is a binomial probability problem.

# Upgrade to premium to receive in-depth solutions to each problem.

'''

Each gasket has a 99% percent chance of being okay,
there are 20 gaskets in a pack, and the chance of being
broken are independent.

So the chance a pack will have no broken gaskets is .99^20
which is roughly 82%.

This means that 18% of packs will need to be replaced.
This could be a bad policy if customers are willing to complain.
That said, 1% failure rate seems super high.
'''
