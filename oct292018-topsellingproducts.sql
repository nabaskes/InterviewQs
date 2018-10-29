-- Question 48 - Top selling products

-- You’re an analyst for an e-commerce store. You’re trying to identify the top selling products in Q4 2017 by region. You have 2 tables that you can query.

-- Table: all_products
-- Column Name 	Data Type 	Description
-- product_id 	integer 	id of the product
-- product_name 	string 	name of the product
-- sku 	integer 	universal stockkeeping unit number
-- distributor_id 	integer 	unique id for distributor

-- Table: orders
-- Column Name 	Data Type 	Description
-- date 	string 	format is "YYYY-MM-DD"
-- user_id 	integer 	user id of purchaser
-- order_id 	integer 	unique order number
-- product_id 	integer 	id of product
-- no_units 	integer 	number of units sold in the order
-- price 	integer 	price per item
-- shipping_id 	integer 	id of shipping information
-- region 	string 	region of shipping id

-- Write a SQL query to find the top 5 selling products by region. Include both the distributor id as well as the name of the product in your results.

-- Upgrade to premium to receive in-depth solutions to each problem.


WITH product_aggregate as
SELECT region, o.product_id as product_id, distributor_id, sum(price) as revenue
FROM orders as o
JOIN all_products
ON o.product_id = all_products.product_id
GROUP BY region, o.product_id, distributor_id

SELECT region, regional_rank
FROM
(SELECT region
	, RANK() OVER (PARTITION BY region ORDER BY revenue) as regional_rank
FROM product_aggregate) as aggregate_ranks
WHERE regional_rank < 5
ORDER BY region;
