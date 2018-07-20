-- Active users on a messaging application

-- Below is a table schema for a P2P messaging application. The table contains send/receive message data for the application's users.



-- table name: user_messaging


-- Field name                       # description


-- time_stamp (integer)             # timestamp, epoch seconds


-- sender_id (integer)              # id of the message sender


-- receiver_id (integer)            # id of the message receiver



-- Question: What fraction of active users communicate with at least 15 unique people on March 1, 2018? Solution will be provided in Python for premium users.

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT cast(sum(is_heavy_user) as real)/cast(count(distinct u.sender_id) as real)
FROM (select distinct sender_id from user_messaging) as  u
JOIN (SELECT sender_id, case when count(receiver_id) > 15 then 1 else 0 end as is_heavy_user
FROM user_messaging
GROUP BY sender_id) as h
ON u.sender_id = h.sender_id
