-- Question 72 - Shoe prices

-- Suppose you are given a SQL table containing the brands of shoes (field name: brand) as well as the shoe price (field name: price). The database is called shoe_info. You are tasked with updating the prices in this database for a few brands of shoes. Specifically, you have been asked to update all Nike shoe prices to $100, and all Adidas shoe prices to $85. Using SQL, write a query to perform this action.

-- Upgrade to premium to receive in-depth solutions to each problem.

-- it might be better to do this as two updates, but we could also do

UPDATE shoe_info SET price=CASE WHEN brand='Nike' THEN 100 ELSE CASE WHEN brand='Adidas' THEN 85 ELSE price END END;
