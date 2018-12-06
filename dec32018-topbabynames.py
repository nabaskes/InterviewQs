# Question 63 - Baby names

# Suppose you are given a dataset of Baby names. Using the dataset, you're tasked with figuring out the top boy and girl names in 2009.
# Can you describe how you would do this using Python Pandas? The solution will be Python code which walks through the logic and calculation.

# Upgrade to premium to receive in-depth solutions to each problem.

# Sample data
''',Id,Name,Year,Gender,State,Count
11349,11350,Emma,2004,F,AK,62
11350,11351,Madison,2004,F,AK,48
11351,11352,Hannah,2004,F,AK,46
11352,11353,Grace,2004,F,AK,44
11353,11354,Emily,2004,F,AK,41
11354,11355,Abigail,2004,F,AK,37
11355,11356,Olivia,2004,F,AK,33
11356,11357,Isabella,2004,F,AK,30
11357,11358,Alyssa,2004,F,AK,29
11358,11359,Sophia,2004,F,AK,28
11359,11360,Alexis,2004,F,AK,27
'''
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

top_names = df[df['Year'] == 2009].sort_values(by=['Count'], ascending=False)

# i feel like splitting by gender could be done in one step
top_boy_name = top_names[top_names['Gender'] == 'M'].iloc[0]
top_girl_name = top_names[top_names['Gender'] == 'F'].iloc[0]
