-- Question 64 - Reddit posts and comments

-- Suppose you're working for Reddit as an analyst. Reddit is trying to optimize its server allocation per subreddit, and you've been tasked with figuring out how much comment activity happens once a post is published.

-- Use your intuition to select a timeframe to query the data as well as how you would want to present this information to the partnering team. The solution will be a SQL query with assumptions that you would need to state if this was asked in an interview. You have the following tables:

-- Table: posts
-- Column Name 	Data Type 	Description
-- id 	integer 	id of the post
-- publisher_id 	integer 	id the user posting
-- score 	integer 	score of the post
-- time 	integer 	post publish time in unixtime
-- title 	string 	title of the post
-- deleted 	boolean 	is the post deleted?
-- dead 	boolean 	is the post active?
-- subreddit_id 	integer 	id of the subreddit


-- Table: comments
-- Column Name 	Data Type 	Description
-- id 	integer 	id of the comment
-- author_id 	integer 	id of the commenter
-- post_id 	integer 	id of the post the comment is nested under
-- parent_comment 	integer 	id of parent comment that comment is nested under
-- deleted 	integer 	is comment deleted?

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT subreddit_id, AVG(num_comments)
FROM
(SELECT posts.id as post_id, count(comments.id) as num_comments, subreddit_id
FROM posts
LEFT JOIN comments
ON posts.id = comments.post_id
GROUP BY posts.id, subreddit_id) as post_activity
GROUP BY subreddit_id
ORDER BY AVG(num_comments) DESC;

-- it doesn't look like we have any timestamp data on comments, so we can't
-- remove extraneous thread-necromancy type comments

-- the subquery seems like information we'd want a lot, so it might make sense
-- to save this as a CTE
