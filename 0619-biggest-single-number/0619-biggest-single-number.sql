# Write your MySQL query statement below
WITH SingleNumbers AS (
    SELECT num 
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)
SELECT max(num) AS num
FROM SingleNumbers
