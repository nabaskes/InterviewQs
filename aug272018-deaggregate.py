# Question 21 - Expanding a data set

# You're given a set of data that is aggregated on a monthly basis (as illustrated in Table A).

# Can you write code that can expand this monthly table into a daily table that spreads revenue across the 30 day period (as shown in Table B)?

# You can assume each month has 30 days and that Table A is in a dataframe named "df".
# Table A

# index 	Month 	Revenue ($)
# 0 	1 	300
# 1 	2 	330
# 2 	3 	390


# Table B

# index 	Month 	Day 	Revenue ($)
# 0 	1 	1 	10
# 1 	1 	2 	10
# 2 	1 	3 	10
# ... 	... 	... 	...
# 30 	2 	1 	11
# 31 	2 	2 	11
# ... 	... 	... 	...
# 60 	3 	1 	13
# ... 	... 	... 	...
# 89 	3 	30 	13

# The solution will be provided in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem

import pandas as pd

def deaggregate(df):
    new_df = pd.DataFrame(data={k: [] for k in df.columns})
    for row in df.iterrows():
        step_df = pd.DataFrame(date={k: [] for k in df.columns}):
        for i in range(1, 30):
            row['Day'] = i
            row['Revenue'] = row['Revenue'] / 30
            step_df.append(pd.DataFrame([row]))
        new_df.append(step_df)
    return new_df
