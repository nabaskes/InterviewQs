# Question 73 - Testing the toxicity of water

# Suppose you're trying to measure the Selenium toxicity in your tap water, and obtain the following values for each day:

# day 	selenium
# 1 	0.051
# 2 	0.0505
# 3 	0.049
# 4 	0.0516
# 5 	0.052
# 6 	0.0508
# 7 	0.0506

# The maxiumum level for safe drinking water is 0.05 mg/L -- using this as your alpha, does the selenium tap level exceed the legal limit? Hint: you can use a t-test here

# Upgrade to premium to receive in-depth solutions to each problem.

import pandas as pd
from scipy import stats
from math import sqrt

df = pd.read_csv('text_data.txt')
N = df.shape[0]
xbar = df['selenium'].mean()
sd = df['selenium'].std()

t, p = stats.ttest_1samp(df['selenium'], 0.05)
min_conf_int = xbar - t * (sd/sqrt(N))
max_conf_int = xbar + t * (sd/sqrt(N))

if min_conf_int > .05:
    print("95% sure that water is unsafe")
elif max_conf_int < .05:
    print("95% sure that water is safe")
else:
    print(f"Water could be safe, sample mean is {xbar} with standard deviation of {sd}")
