# Question 17 - Analyzing employee data using Python

# Below is a snippet from a table that contains information about employees that work at Company XYZ:
# Column name 	Data type 	Example value 	Description
# employee_name 	string 	Cindy 	Name of employee
# employee_id 	integer 	1837204 	Unique id for each employee
# yrs_of_experience 	integer 	14 	total working years of experience
# yrs_at_company 	integer 	10 	total working years at Company XYZ
# compensation 	integer 	100000 	dollar value of employee compensation
# career_track 	string 	technical 	Potential values: technical, non-technical, executive

# Company XYZ Human Resource department is trying to understand compensation across the company and asked you to pull data to help them make a decision regarding employee compensation.

# Question: Can you pull the average, median, minimum, maximium, and standard deviations for salary across 5 year experience buckets at Company XYZ? (e.g. get the corresponding average, median, minimum, maximium, and standard deviations for expereience buckets 0-5, 5-10, 10-15, ect.) You can assume the data is imported into a dataframe named df. Solution will be provided in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.

import math
import pandas as pd

def summary_statistics(df):
    def bucket_by_five(year):
        return math.floor(year / 5)
    summary_df = pd.DataFrame()
    summary_df['min'] = df.groupby(bucket_by_five).min()
    summary_df['max'] = df.groupby(bucket_by_five).max()
    summary_df['std'] = df.groupby(bucket_by_five).std()
    summary_df['mean'] = df.groupby(bucket_by_five).mean()
    return summary_df
