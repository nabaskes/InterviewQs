-- Question 37 - Employees who are managers

-- Suppose you're trying to understand how many managers you have per employee at Company XYZ. On your search to understand, you are given two tables: (1) managers and (2) employees. Each table has 1 column named id.

-- Given this dataset, can you use SQL to find the employees that are also managers? Hint: given the table names as well as the single column name you should be able to write a full SQL query.

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT e.employee_id, e.name
FROM employees e
INNER JOIN managers m
ON e.employee_id = m.employee_id

-- are the sql questions getting easier?
