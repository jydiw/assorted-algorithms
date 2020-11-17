/*
Assume you are given the below table on purchases from users. Write a query to
get the number of people that purchased at least one product on multiple days.

purchases
column_name	    type
purchase_id	    integer
user_id	        integer
product_id	    integer
quantity	      integer
price	          float
purchase_time	  datetime
*/

-- begin cte
WITH frequent AS (
  SELECT user_id
       , RANK() OVER (
           PARTITION BY user_id, product_id
           ORDER BY purchase_time
         ) AS num_purchases
    FROM purchases
)

SELECT COUNT(DISTINCT user_id)
  FROM frequent
 WHERE num_purchases >= 2