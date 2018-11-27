# data: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv
# order_id	quantity	item_name	choice_description	item_price
# 1	1	Chips and Fresh Tomato Salsa	NULL	$2.39
# 1	1	Izze	[Clementine]	$3.39
# 1	1	Nantucket Nectar	[Apple]	$3.39


# Question 59 - Chipotle item analysis

# You are given a data set of Chipotle orders. You're asked to figure out the average order price and the average price per item ordered. Can you describe how you would do this using Python Pandas? The solution will be Python code which walks through the logic and calculation.

# Upgrade to premium to receive in-depth solutions to each problem.


def get_all_numeric(value):
    return float(''.join(v for v in value if v.isdigit() or v=="."))

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')
df['item_price'] = df['item_price'].apply(get_all_numeric)
print(df['item_price'])

avg_order_price = df.groupby('order_id')['item_price'].sum().mean()
print("Avg order price is ", end="")
print(avg_order_price)

total_cost = df['item_price'].sum()
total_quantity = df['quantity'].sum()
avg_price_per_item = total_cost/total_quantity
print("Avg price per item is ", end="")
print(avg_price_per_item)
