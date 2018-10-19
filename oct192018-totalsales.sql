-- Question 44 - Joining to get total sales, a SQL problem

-- Suppose you work for a retail company that has a database containing two tables, one called 'orders', and one called 'revenue', as shown below:

-- Orders:
-- 	order_id 	channel 	date 	month
-- 0 	1 	Online 	2018-09-01 	September
-- 1 	2 	Online 	2018-09-03 	September
-- 2 	3 	In_store 	2018-10-11 	October
-- 3 	4 	In_store 	2018-08-21 	August
-- 4 	5 	Online 	2018-08-13 	August
-- 5 	6 	Online 	2018-10-29 	October

-- Revenue:
-- 	order_id 	revenue
-- 0 	1 	100
-- 1 	2 	125
-- 2 	3 	200
-- 3 	4 	80
-- 4 	5 	200
-- 5 	6 	100

-- Using SQL, write a query to show the total revenue by channel for the months of September and October. Additionally, try to think of the most efficient way to run this query.

SELECT month, sum(revenue)
FROM (
     SELECT order_id, channel, month
     FROM Orders
     WHERE month in ('September', 'October')) as sept_oct_orders as o
INNER JOIN Revenue as r
ON o.order_id = r.order_id
GROUP BY month, channel

-- this is an efficient solution for large search space.
-- If orders is really large, we do well by first restricting to September
-- and October.  Hopefully the month column is indexed.

-- Then, we join on the almost certainly indexed order_id column.
-- Since this is an inner join, it may further restrict the size of the
-- data in memory if there are orders without revenue.

-- Finally, we group by month and channel.
-- This time, hopefully channel is indexed

-- The length of time here should be on the order of
--    log(count(Orders)) + count(Orders in Oct or Sept) * log(count(Revenue))
--    + log(count(Revenue in Oct or Sept w/ orders))
