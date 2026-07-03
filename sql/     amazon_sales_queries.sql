CREATE DATABASE amazon_sales;
USE amazon_sales;

-- TOTAL ORDERS;
SELECT COUNT(*) AS Total_orders
FROM amazon_sales_sample;

-- TOTAL REVENUE;
SELECT ROUND(SUM(AMOUNT),2) AS Total_Revenue
FROM amazon_sales_sample;

-- AVERAGE ORDER VALUE;
SELECT ROUND(AVG(AMOUNT),2) AS Average_order_value
FROM amazon_sales_sample;

-- TOTAL QUANTITY SOLD;
SELECT SUM(Qty) AS Total_quantity
From amazon_sales_sample;

-- NUMBER OF CATEGORIES;
select COUNT(DISTINCT Category) AS Categories
FROM amazon_sales_sample;

-- NUMBER OF STATES;
SELECT COUNT(DISTINCT 'ship-state') AS states
FROM amazon_sales_sample;

-- SALES BY CATEGORY
SELECT
Category,
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY Category
ORDER BY Revenue DESC;

-- TOP 10 STATES;
SELECT
'ship-state',
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY 'ship-state'
ORDER BY Revenue DESC
LIMIT 10;

-- TOP 10 CITIES;
SELECT
'ship-city',
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY 'ship-city'
ORDER BY Revenue DESC
LIMIT 10;

-- ORDER STATUS
SELECT
status,
COUNT(*) AS orders
FROM amazon_sales_sample
GROUP BY status
ORDER BY orders DESC;

-- FULLFILLMENT ANALYSIS;
SELECT
Fulfilment,
ROUND(SUM(AMOUNT),2) AS REVENUE,
COUNT(*) AS orders
FROM amazon_sales_sample
GROUP BY Fulfilment;

-- MONTHLY SALES
SELECT
Month,
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY Month
ORDER BY 'Month number';

-- BEST SELLING PRODUCTS
select
SKU,
SUM(Qty) AS Quantity
FROM amazon_sales_sample
GROUP BY SKU
ORDER BY Quantity DESC
LIMIT 10;

-- REVENUE SIZE
SELECT
size,
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY size
ORDER BY Revenue DESC;

-- REVENUE BY COURIER STATUS
SELECT
'courier status',
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY 'Courier Status'
ORDER BY Revenue DESC;

-- TOP SELLING STYLES
SELECT
style,
SUM(Qty) AS Quantity
FROM amazon_sales_sample
GROUP BY style
ORDER BY Quantity DESC
LIMIT 10;

-- REVENUE BY SALES CHANNEL
SELECT
'sales channel',
ROUND(SUM(AMOUNT),2) AS Revenue
FROM amazon_sales_sample
GROUP BY 'sales channel'
ORDER BY Revenue DESC;