# Question 55 - Categorizing foods

# You are given the following dataframe and are asked to cateogrize each food into 1 of 3 categories: meat, fruit, or other.
# 	food 	pounds
# 0 	bacon 	4.0
# 1 	STRAWBERRIES 	3.5
# 2 	Bacon 	7.0
# 3 	STRAWBERRIES 	3.0
# 4 	BACON 	6.0
# 5 	strawberries 	9.0
# 6 	Strawberries 	1.0
# 7 	pecans 	3.0

# Can you add a new column containing the foods' categories to this dataframe using python?

# Upgrade to premium to receive in-depth solutions to each problem.


def get_food_group(name):
    name = name.lower()
    if FRUIT_DICT.get(name) is not None:
        return 'fruit'
    if MEAT_DICT.get(name) is not None:
        return 'meat'
    return 'other'


def categorize_food(df):
    df['food_category'] = df['food'].apply(get_food_group)
    return df

# im not gonna waste time making a dict of all food names right now.
