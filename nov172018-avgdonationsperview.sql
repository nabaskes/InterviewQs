-- Question 56 - Twitch content creators

-- Suppose you are working for a company like Twitch.tv. Twitch.tv is a live streaming platform, where content creators (e.g. the people creating content on the live streams) can receive donations from viewers for producing content they support.

-- Your company is trying to launch a new product that will benefit content creators who get a large amount of donations per streaming session.

-- Can you write a SQL query to find the top 10 content creators in 2018 that have had the highest average donations per viewer?

-- You are given the following tables:

-- Table: all_donations
-- Column Name 	Data Type 	Description
-- creator_id 	integer 	unique id of content creator
-- viewer_id 	integer 	unique id of viewer
-- session_id 	integer 	unique session id of stream
-- date 	string 	format is "YYYY-MM-DD"
-- donation_amount 	integer 	amount donated in USD

-- Table: sessions_info
-- Column Name 	Data Type 	Description
-- creator_id 	integer 	unique id of content creator
-- session_id 	integer 	unique id of viewer
-- date 	string 	format is "YYYY-MM-DD", date of session
-- length 	integer 	length of session

-- Table: session_viewers
-- Column Name 	Data Type 	Description
-- creator_id 	integer 	unique id of content creator
-- viewer_id 	integer 	unique id of viewer
-- date 	string 	format is "YYYY-MM-DD"
-- session_id 	integer 	unique session id of stream
-- mins_viewed 	integer 	total number of the viewer watched the stream

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT top 10 s.creator_id
, cast(total_donations as real)/cast(num_viewers as real) as avg_donations_per_viewer
FROM sessions_info s
LEFT JOIN (SELECT creator_id, sum(donation_amount) as total_donations
FROM all_donations
GROUP BY creator_id) as donations
ON s.creator_id = donations.creator_id
LEFT JOIN
(SELECT creator_id, count(viewer_id) as num_viewers
FROM session_viewers
GROUP BY creator_id) as viewers
ON s.creator_id = viewers.creator_id
GROUP BY s.creator_id
ORDER BY avg_donations_per_viewer DESC
