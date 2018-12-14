# Question 67 - Drop rows in dataframe that are between two dates

# Given the following dataframe, df, drop all the rows where the contract_sign_date is between 2018-09-01 and 2018-10-13 (inclusive):

# df:
# 	vendor_id 	name 	contract_sign_date 	total_spend
# 0 	1 	vendor_schmendor 	2018-09-01 	34324
# 1 	2 	parts_r_us 	2018-09-03 	23455
# 2 	3 	vendor_king 	2018-10-11 	77654
# 3 	4 	vendor_diagram 	2018-08-21 	23334
# 4 	5 	venny 	2018-08-13 	94843
# 5 	6 	vendtriloquist 	2018-10-29 	23444

# Solution will be written using Python (Pandas).

# Upgrade to premium to receive in-depth solutions to each problem.

df = df[df['contract_sign_date'] < '2018-10-13'][df['contract_sign_date'] > '2018-09-01']
