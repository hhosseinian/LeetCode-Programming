# Write your MySQL query statement below
SELECT E1.name AS name
FROM Employee E1
LEFT JOIN Employee E2
ON E1.id = E2.managerId
GROUP BY E1.id
HAVING COUNT(E2.managerId) >= 5;
