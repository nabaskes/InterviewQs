-- Question 69 - Airbnb stays by country

-- Suppose you work for Airbnb as an analyst. A team has come to you asking for a ranked list containing total # stays as well as total revenue, split by country. The time frame they're looking for is all stays that began in 2018. You can sort the list in descending order by revenue.

-- The table schemas are provided below. Using SQL, write a query to answer this question.

-- Table: property_location_info
-- Column Name 	Data Type 	Description
-- property_id 	integer 	ID of the property location
-- country 	string 	country code of the property location
-- city_name 	string 	name of city (note there can be multiple cities with the same name)
-- subregion_name 	string 	provience, state, or subregion name
-- address 	string 	address of property location

-- Table: stays_info
-- Column Name 	Data Type 	Description
-- guest_id 	integer 	ID of guest
-- property_id 	integer 	ID of the property location
-- host_id 	integer 	ID of the host manging the property
-- revenue 	integer 	cost of stay for guest in USD
-- date_start 	string 	start day of stay, format is "YYYY-mm-dd"
-- date_end 	string 	end day of stay, format is "YYYY-mm-dd"
-- stay_length 	integer 	number of days for the stay
-- airbnb_revenue 	integer 	revenue that Airbnb collected on stay


-- Upgrade to premium to receive in-depth solutions to each problem.

select country, count(si.property_id), sum(si.revenue)
FROM property_location_info as pli
inner join stays_info as si
ON pli.property_id = si.property_id
WHERE date_start LIKE '2018%'
GROUP BY country
ORDER BY sum(si.revenue) DESC
