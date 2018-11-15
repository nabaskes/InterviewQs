-- Question 53 - Planning for a new office location, using SQL

-- Suppose you work for a retail company and have access to two tables:

-- Customers:
-- customer_id 	city
-- 0 	New York
-- 1 	New York
-- 2 	Los Angeles
-- 3 	Jacksonville

-- Suppliers:
-- supplier_id 	city
-- 0 	Omaha
-- 1 	New York
-- 2 	San Francisco
-- 3 	Los Angeles

-- You've been tasked to find which cities have a strong overlap with both customers and suppliers, as your company explores opening an additional office. Using SQL, write a query to stack rank the frequency of the cities shown across both databases.

-- Your query should return the following elements:

--     City
--     # of times city appeared across both tables

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT case when c.city is not NULL then c.city else s.city end
, num_customers + num_suppliers as num_contacts
FROM
(select city, count(customer_id) as num_customers
from Customers
group by city) as c
FULL OUTER JOIN (select city, count(supplier_id) as num_suppliers
from Suppliers
group by city) as d
ON c.city = d.city
