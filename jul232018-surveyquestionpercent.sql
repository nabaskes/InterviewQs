-- Employee survey results

-- You're consulting for a company, and you've sent out a survey that asks successive qustions randomly. The survey logs data into a table called survey_logging. The schema of the table is:

-- Column Name 	Data Type 	Description
-- employee_id 	integer 	employee id of the survey respondant
-- action 	string 	Will be one of the following values, 'view', 'answer', 'skip'
-- question_id 	integer 	ID of the question asked
-- answer_id 	integer 	ID of the answer asked
-- timestamp 	integer 	time stamp of the action made by respondant


-- Question: Using SQL, find which question has the highest response rate.

-- Upgrade to premium to receive in-depth solutions to each problem.

SELECT TOP 1 CAST(SUM(CASE WHEN action='answer' THEN 1 ELSE 0 END) AS REAL)/CAST(COUNT(employee_id) as REAL) as AnswerPercentage
FROM survey_logging
GROUP BY question_id
ORDER BY AnswerPercentage DESC
