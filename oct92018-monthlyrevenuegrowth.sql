-- Question 40 - Calculating monthly revenue growth in SQL

-- Given the table below, called 'orders', write a SQL query to show the monthly revenue growth. To calculate the monthly revenue growth, you can apply the following logic:

-- revenue growth = (current month's revenue-prior month's revenue)/prior month's revenue.
-- order_id 	channel 	date 	month 	revenue
-- 1 	online 	2018-09-01 	09 	100
-- 2 	online 	2018-09-03 	09 	125
-- 3 	in_store 	2018-10-11 	10 	200
-- 4 	in_store 	2018-08-21 	08 	80
-- 5 	online 	2018-08-13 	08 	200

-- Upgrade to premium to receive in-depth solutions to each problem.




SELECT (current_revenue - previous_revenue)/previous_revenue as monthly_revenue_growth
FROM (
     SELECT
cast(sum(case when month(date)=month(curdate()) then revenue else 0 end) as float) as current_revenue
, cast(sum(case when month(date)=month(curdate()) - 1 then revenue else 0 end)) as float) as previous_revenue
FROM orders) as monthly_revenues


-- i hate this table, the columns are named the same as keywords
-- i manually extracted the month from the date rather than using the given one
-- change curdate() to getdate() to convert from mysql to sql server

-- if you want to use postgres or sqlite you'll need to finagle about with
-- extract to get months or strfdate to get months, respectively
