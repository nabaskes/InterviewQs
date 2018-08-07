--  question 10 - Calculating student attendance using SQL

-- Given the following table schemas, how would you figure out the overall attendance rate for each grade on 2018-03-12? Answers will be provided in SQL for premium users.

-- Table 1: student_attendance_log
-- Column Name 	Data Type 	Description
-- date 	string 	date of log per student_id, format is 'yyyy-mm-dd'
-- student_id 	integer 	id of the student
-- attendance_status 	string 	Possible values are ['present', 'tardy', 'absent']

-- Table 2: student_demographic
-- Column Name 	Data Type 	Description
-- student_id 	integer 	id of the student
-- grade_level 	integer 	will be a value between 0-12, which corresponds
-- date_of_birth 	string 	Student birth date, format is 'yyyy-mm-dd'

-- Upgrade to premium to receive in-depth solutions to each problem.


SELECT grade_level, cast(sum(case when attendance_status is not 'absent' then 1 else 0 end) as real)/cast(count(*) as real)
FROM student_demographic d
JOIN student_attendance_log a
ON d.student_id = a.student_id
GROUP BY grade_level
ORDER BY grade_level DESC
