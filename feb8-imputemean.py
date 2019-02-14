# Question 91 - Replacing bad data with Pandas

# Suppose you are given a dataframe, df, that contains various negative values. In the context of your work, negative values can be considered 'bad data'. Write a function in Python (using Pandas) that replaces these bad values with the group mean.

# Solution will be written in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


import pandas as pd


def impute_negative_to_mean(df):
    for col in df.columns:
        df[df[col] < 0] = df[df[col] >= 0][col].mean()
    return df
# god, i love pandas, you can do complicated things really simply and in a way that is really hard to read
