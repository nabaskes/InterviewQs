-- Question 18 - A hotel chain's loyal customers

-- You are an analyst for a major US hotel chain which has locations all over the US. Your marketing team is planning a promotion focused around loyal customers, and they are trying to forecast how much revenue the promotion will bring in. However, they need help from you to understand how much revenue comes from "loyal" customer to plug into their model.

-- A "loyal" customer is defined as (1) having a memebership with your company's point system, (2) having >2 stays at each hotel the customer visited, (3) having stayed at 3 different locations throughout the US.

-- You have a table showing all transactions made in 2017. The schema of the table is below:

-- Table: customer_transactions
-- Column Name 	Data Type 	Description
-- customer_id 	id 	id of the customer
-- hotel_id 	integer 	unique id for hotel
-- transaction_id 	integer 	id of the given transaction
-- first_night 	string 	first night of the stay, column format is "YYYY-mm-dd"
-- number_of_nights 	integer 	# of nights teh customer stayed in hotel
-- total_spend 	integer 	total spend for transaction, in USD
-- is_memeber 	boolean 	indicates if the customer is a member of our points system

-- Can you write a query that calculates percent of revenue loyal customers brought in 2017? Answer will be provided tomorrow in SQL for premium users.

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT CAST(SUM(
       CASE WHEN is_memeber=True
       AND number_of_stays > 2
       AND number_of_hotels > 3
       THEN number_of_nights
       ELSE 0
       END) as REAL)/CAST(SUM(number_of_nights) as REAL)
FROM customer_transactions
JOIN (SELECT customer_id,
     count(customer_id) as number_of_stays,
     count(distinct hotel_id) as number_of_hotels
     FROM customer_transactions
     GROUP BY customer_id) as customer_stats
ON customer_transactions.customer_id = customer_stats.customer_id
