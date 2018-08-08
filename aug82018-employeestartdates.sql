-- Question 13 - Cleaning and analyzing employee data

-- Below is a snippet from a table that contains information about employees that work at Company XYZ:

-- employee_name 	employee_id 	date_joined 	age 	yrs_of_experience
-- Andy 	123456 	2015-02-15 	45 	24
-- Beth 	789456 	NaN 	36 	15
-- Cindy 	654123 	2017-05-16 	34 	14
-- Dale 	963852 	2018-01-15 	25 	4

-- Company XYZ recently migrated database systems causing some of the date_joined records to be NULL.
-- You're told by an analyst in human resources NULL records for the date_joined field indicates the employees joined prior to 2010.
-- You also find out there are multiple employees with the same name as well as duplicate records for some employees.

-- Question:
-- Can you write code using Python and the Pandas library that finds the number of employees that joined each month?
-- You can group all of the NULL values as having joined on Dec 1, 2009.

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT MONTH(start_date), COUNT(employee_id)
FROM (SELECT employee_id,
      min(start_date)
      FROM (SELECT employee_id, CASE date_joined is not null then date_joined else '2009-12-01' END as start_date) as cleaned_dates
      GROUP BY employee_id) as employee_records
GROUP BY MONTH(start_date)
