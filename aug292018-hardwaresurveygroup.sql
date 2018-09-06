--  Question 22 - Picking a survey group

-- You work for a large hardware company (one that manufactures watches, computers, and phones) and you're trying to understand user sentiment towards the company's brand and the products. You decide to send out a survey to a random set of users across different products.

-- Can you create a query that samples across the different product offerings? The output of your query should be user_id and group (e.g. the sampling group the user belongs to).

-- You have a table with all users and their registered devices. The schema of the table is below:

-- Table: user_devices
-- Column Name 	Data Type 	Description
-- user_id 	integer 	id of the user
-- devices 	array of strings 	lists the devices (watch, computer, phone)
-- device_ids 	array of integers 	id of the devices used by the user
-- user_create_time 	integer 	epoch time of the user's account
-- total_spend 	integer 	lifetime spend of a user
-- country 	string 	user country

-- Solution will be provided using SQL for premium users.

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT user_id, device_name
FROM (SELECT TOP @sample_size user_id, 'WATCH' as device_name
     FROM user_devices
     WHERE devices LIKE 'WATCH'
     ORDER BY RAND()
     UNION
     SELECT TOP @sample_size user_id, 'COMPUTER' as device_name
     FROM user_devices
     WHERE devices LIKE 'COMPUTER'
     ORDER BY RAND()
     UNION
     SELECT TOP @sample_size user_id, 'PHONE' as device_name
     FROM user_devices
     WHERE devices LIKE 'PHONE')

-- Note: this is an example where you should definitely do a bit of
-- data engineering.  This process could be a lot more extendable if there
-- was a separate "devices" table basically correlating devices to ids,
-- and a UserDeviceMapping table with an entry for every devise each user has
