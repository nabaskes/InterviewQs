-- Question 80 - Days to first sale

-- You’re working as a analyst for a sales organization and you’re asked to figure out how long it takes for a sales representative to make their first sale. You’re also given the following tables:

-- Table 1: sales_rep_info
-- column 	description
-- sales_rep_id 	unique sales rep identifier
-- date_hired 	hire date of employee, format 'YYYY-MM-DD'
-- product_focus_area 	types of products the rep sells
-- tenure 	total yrs of sales experience
-- level 	employee level at the company

-- Table 2: all_sales
-- column 	description
-- date 	close date of sale, format 'YYYY-MM-DD'
-- purchase_order_number 	unique identier for the sale
-- buyer_id 	the unique identifer for buyer
-- sales_rep_id 	unique sales rep identifier of the
-- order_price_usd 	total sales price in USD
-- date_sale_initiated 	date the purchase order
-- was initiated, format 'YYYY-MM-DD'

-- Can you write a SQL query that shows how long it takes for a sales representative to make their first sale?


-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT sales_rep_id, DATEDIFF(date_hired, first_sale_date) as days_to_first_sale
FROM sales_rep_info r
INNER JOIN (SELECT sales_rep_id, min(date_sale_initiated) as first_sale_date
FROM all_sales
GROUP BY sales_rep_id) s
ON s.sales_rep_id = r.sales_rep_id;
