# Write your MySQL query statement below
SELECT E1.employee_id, E1.name, COUNT(E2.employee_id) AS reports_count, ROUND(AVG(E2.age),0) AS average_age
FROM Employees E1
RIGHT JOIN Employees E2
ON E2.reports_to = E1.employee_id
WHERE E1.employee_id IS NOT NULL
GROUP BY E1.employee_id
ORDER BY E1.employee_id;