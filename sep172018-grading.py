# Question 30 - Assigning grades

# You are given a dataframe (df) of students, and you need to assign grades to each student. The table schema is as follows:
# Column name 	Data type 	Example value 	Description
# student_name 	string 	Cindy Chu 	Name of student
# student_id 	integer 	1837204 	Unique id for each student
# class 	string 	Biology 	Name of class
# final_grade_pct 	integer 	80 	final grade for class represented in percent


# You need to assign the following letter grades based on final_grade_pct in a new column named "final_grade_letter":

#     >90 - A
#     81-90 - B
#     71-80 - C
#     <70 - D

# Write a function using Python to loop through the table and assign the appropriate letter grades to each student, adding a new column to the existing dataframe, df.

# Upgrade to premium to receive in-depth solutions to each problem.

import pandas as pd


def grade_students(df: pd.DataFrame) -> pd.DataFrame:
    def assign_grade(score: float) -> str:
        if score > 90:
            return "A"
        elif score >= 81:
            return "B"
        elif score >= 71:
            return "C"
        return "D"
    # coddled kids nowaday not getting Fs?

    df['final_grade_letter'] = df['final_grade_pct'].apply(assign_grade)
    return df

# i'm not sure what the point here is, do we just need to know the apply method?
