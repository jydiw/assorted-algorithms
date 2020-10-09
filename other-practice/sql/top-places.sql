/*
Assume you are given the below table on reviews from users. Define a top-rated
place as a business whose reviews only consist of 4 or 5 stars. Write a query
to get the number and percentage of businesses that are top-rated places.

reviews
column_name	  type
business_id	  integer
user_id	      integer
review_text	  string
review_stars	integer
review_date	  datetime
*/

WITH top_rated AS (
    SELECT business_id
      FROM reviews
     GROUP BY business_id
           HAVING SUM(CASE WHEN review_stars >= 4 THEN 1 ELSE 0) = COUNT(*)
)

SELECT COUNT(DISTINCT t.business_id) AS num_top_rated
     , COUNT(DISTINCT t.business_id) / COUNT(DISTINCT r.business_id) AS pct_top_rated
  FROM reviews as r
       LEFT JOIN top_rated AS t
              ON r.business_id = t.business_id