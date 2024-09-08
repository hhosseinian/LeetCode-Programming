# Write your MySQL query statement below
SELECT R.contest_id, ROUND(100*COUNT(DISTINCT R.user_id)/(SELECT COUNT(*) FROM Users),2) AS percentage
From Register R
#LEFT JOIN Users U
#ON U.user_id = R.user_id
GROUP BY R.contest_id
ORDER BY percentage DESC,
R.contest_id ASC;