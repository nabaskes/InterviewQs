'''
Question 43 - Revenue trends for online vs. in store channels

Given the table below, called 'orders', write code to show the average revenue by month by channel:
order_id 	channel 	date 	month 	revenue
1 	online 	2018-09-01 	09 	100
2 	online 	2018-09-03 	09 	125
3 	in_store 	2018-10-11 	10 	200
4 	in_store 	2018-08-21 	08 	80
5 	online 	2018-08-13 	08 	200

Your result should return the following in a structured table:

Month | Channel | Avg. Revenue

Solution will be provided in Python for premium users.
'''


def avg_revenue_by_month_by_channel(orders):
    return orders.groupby(['month', 'channel'])['revenue'].mean()


def sql_solution(orders):
    from pandasql import sqldf

    def pysqldf(q): sqldf(q, globals())
    q = """SELECT avg(revenue)
    FROM orders
    GROUP BY month, channel
    """
    return pysqldf(q)
