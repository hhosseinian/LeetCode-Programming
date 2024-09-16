# Write your MySQL query statement below
WITH last as(
    SELECT product_id,new_price,change_date
    FROM Products P
    WHERE P.change_date = (SELECT max(change_date)FROM PRODUCTS WHERE P.product_id =product_id AND change_date <='2019-08-16')
)
SELECT DISTINCT p.product_id, COALESCE(t.new_price, 10) AS price
FROM Products as p LEFT JOIN last AS t ON p.product_id =t.product_id