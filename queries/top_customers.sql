-- Return top customers by total spend in a date range.
SELECT
  customer_id,
  SUM(amount) AS total_spend
FROM sales
WHERE sale_date >= ? AND sale_date < ?
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT ?;
