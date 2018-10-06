
# Question 38 - Calculating earnings with Python

# Suppose an individual is taxed 30% if earnings for a given week are > = $2,000. If earnings land < $2,000 for the week, the individual is taxed at a lower rate of 15%.

# Write a function using Python to calculate both the pre-tax and post-tax earnings for a given individual, with the ability to feed in the hourly wage and the weekly hours as inputs.

# For example, if an individual earns $55/hour and works for 40 hours, the function should return:

#     Pre-tax earnings were 55*40 = $2,200 for the week.
#     Post-tax earnings were $2,200*.7 (since we fall in higher tax bracket here) = $1,540 for the week

# Solution will be provided in Python to premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


def calculate_earnings(hours: float, hourly_rate: float) -> (float, float):
    gross_earnings = hours * hourly_rate
    if gross_earnings > 2000:
        tax_rate = .3
    else:
        tax_rate = .15
    return gross_earnings, gross_earnings * (1 - tax_rate)


# income tax doesn't actually work the way it's described in the problem
def calculate_earnings_realistic(hours: float, hourly_rate: float) -> (float, float):
    gross_earnings = hours * hourly_rate
    if gross_earnings > 2000:
        net_earnings = 300 + (gross_earnings - 2000) * .7
    else:
        net_earnings = gross_earnings * .85
    return gross_earnings, net_earnings
