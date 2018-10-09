# erik@interviewqs.com via uchicagoedu.onmicrosoft.com

# Mon, Oct 8, 11:33 AM (22 hours ago)

# to nabaskes
# Question 39 - Normalizing student grades with Pandas

# You are given a dataframe containing student information, named df (shown below). Suppose you want to normalize each student's grade based on their age.
# Age 	Favorite Color 	Grade 	Name
# 20 	blue 	88 	Willard Morris
# 19 	blue 	95 	Al Jennings
# 22 	yellow 	92 	Omar Mullins
# 21 	green 	70 	Spencer McDaniel

# Write a function using Python Pandas that will add a new column to your dataframe containing a new grade normalized against the mean age of the students.

def normalize_grade_to_age(df):
    # we assume there are a reasonable number of counts in each age
    mean_scores = df.groupby('Age')['Grade'].mean()
    stdev_scores = df.groupby('Age')['Grade'].std()
    def standard_score(row):
        mean_grade = mean_scores['Age']
        stdev_grade = stdev_scores['Age']
        return (mean_grade - row['Grade'])/stdev_grade
    df['Normalized Grade'] = df.apply(standard_score)
    return df
