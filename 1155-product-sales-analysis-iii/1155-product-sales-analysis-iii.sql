# Write your MySQL query statement below
WITH FirstYearSales AS (
    -- Subquery to find the earliest year for each product
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

-- Join the first-year information with the Sales table to get the details
SELECT s.product_id, 
       f.first_year AS first_year, 
       s.quantity, 
       s.price
FROM Sales s
JOIN FirstYearSales f
ON s.product_id = f.product_id
AND s.year = f.first_year;
