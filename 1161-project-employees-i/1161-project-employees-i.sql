# Write your MySQL query statement below
SELECT P.project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM Project P
JOIN Employee E
ON P.employee_id = E.employee_id
GROUP BY project_id
