-- Question 14 - Popular songs (a SQL question)

-- Below are two table schemas for a popular music streaming application:

-- Table 1: user_song_log
-- Column Name 	Data Type 	Description
-- user_id 	id 	id of the streaming user
-- timestamp 	integer 	timestamp of when the user started listening to the song, epoch seconds
-- song_id 	integer 	id of the song
-- artist_id 	integer 	id of the artist

-- Table 2: song_info
-- Column Name 	Data Type 	Description
-- song_id 	integer 	id of the song
-- artist_id 	integer 	id of the artist
-- song_length 	integer 	length of song in seconds


-- Question:

-- Can you write a SQL query to estimate the average number of hours a user spends listening to music daily?

-- Upgrade to premium to receive in-depth solutions to each problem.


SELECT user_id, (sum(song_length)/3600)/((max(timestamp) - min(timestamp))/86400) as hours_per_day
FROM user_song_log
JOIN song_info
ON user_song_log.song_id = song_info.song_id
GROUP BY user_id
