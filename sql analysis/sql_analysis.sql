-- Import outputs/cleaned_ecommerce_sales.csv into SQL Server as ecommerce_sales.
-- Suggested SQL types: Order ID, CustomerName, State, City, Category,
-- Sub-Category, PaymentMode, Month = VARCHAR; Order Date = DATE;
-- Amount, Profit, Quantity = INT (check import wizard mappings).
-- For easier SQL queries, rename imported column headers to:
-- order_id, amount, profit, quantity, category, sub_category,
-- payment_mode, order_date, customer_name, state, city, month.

-- 1. KPIs
SELECT SUM(amount) AS total_sales, SUM(profit) AS total_profit,
       COUNT(DISTINCT order_id) AS total_orders,
       CAST(SUM(amount)*1.0/NULLIF(COUNT(DISTINCT order_id),0) AS DECIMAL(12,2)) AS avg_order_value
FROM ecommerce_sales;

-- 2. Monthly trend
SELECT [month], SUM(amount) AS sales, SUM(profit) AS profit
FROM ecommerce_sales GROUP BY [month] ORDER BY [month];

-- 3. Category performance
SELECT category, SUM(amount) AS sales, SUM(profit) AS profit
FROM ecommerce_sales GROUP BY category ORDER BY sales DESC;

-- 4. Top 10 customers by sales
SELECT TOP 10 customer_name, SUM(amount) AS sales
FROM ecommerce_sales GROUP BY customer_name ORDER BY sales DESC;

-- 5. Top states
SELECT state, SUM(amount) AS sales, SUM(profit) AS profit
FROM ecommerce_sales GROUP BY state ORDER BY sales DESC;

-- 6. Payment modes
SELECT payment_mode, COUNT(*) AS line_items, SUM(amount) AS sales
FROM ecommerce_sales GROUP BY payment_mode ORDER BY sales DESC;

-- 7. Sub-category performance
SELECT sub_category, SUM(amount) AS sales, SUM(profit) AS profit
FROM ecommerce_sales GROUP BY sub_category ORDER BY sales DESC;

-- 8. Unprofitable sub-categories
SELECT sub_category, SUM(profit) AS profit
FROM ecommerce_sales GROUP BY sub_category HAVING SUM(profit)<0 ORDER BY profit;

-- 9. Monthly order volume
SELECT [month], COUNT(DISTINCT order_id) AS orders
FROM ecommerce_sales GROUP BY [month] ORDER BY [month];

-- 10. Profit margin by category
SELECT category, SUM(amount) AS sales, SUM(profit) AS profit,
       CAST(100.0*SUM(profit)/NULLIF(SUM(amount),0) AS DECIMAL(8,2)) AS profit_margin_pct
FROM ecommerce_sales GROUP BY category ORDER BY profit_margin_pct DESC;
