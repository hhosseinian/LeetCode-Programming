# Write your MySQL query statement below
SELECT employee_id,department_id
FROM Employee
#LEFT JOIN EMPLOYEE E2
#ON E1.employee_id = E2.employee_id
WHERE primary_flag ='Y' OR employee_id IN (SELECT employee_id
FROM Employee
GROUP BY employee_id
HAVING count(employee_id)=1);
#GROUP BY E1.employee_id