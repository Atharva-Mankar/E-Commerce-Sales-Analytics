# E-Commerce Sales Analytics Dashboard

## 📊 Project Overview

This project is an end-to-end E-Commerce Sales Analytics solution developed using SQL Server, Python and Power BI.

The objective of the project is to analyze e-commerce sales data and create an interactive dashboard that provides insights into sales performance, profit, orders, product categories, states, payment methods and customers.

## 🎯 Objectives

- Analyze overall sales performance
- Track total sales and profit
- Analyze monthly sales trends
- Identify sales performance by category
- Analyze sales by state
- Understand customer payment preferences
- Identify top customers based on sales
- Provide an interactive Power BI dashboard

## 🛠️ Technologies Used

- SQL Server
- Microsoft Power BI
- Python
- Pandas
- Matplotlib
- Git & GitHub

## 🗄️ Database Structure

The project uses SQL Server with two main tables:

### Orders
- Order_ID
- Order_Date
- CustomerName
- State
- City

### Details
- Order_ID
- Amount
- Profit
- Quantity
- Category
- Sub_Category
- PaymentMode

The tables are connected using `Order_ID`.

## 📈 Key Metrics

| Metric | Value |
|---|---:|
| Total Sales | 437,771 |
| Total Profit | 36,963 |
| Total Orders | 500 |
| Total Quantity | 5,615 |

## 📊 Dashboard Features

The Power BI dashboard contains:

- Total Sales KPI
- Total Profit KPI
- Total Orders KPI
- Total Quantity KPI
- Monthly Sales Trend
- Sales by Category
- Sales by State
- Sales by Payment Mode
- Top 5 Customers by Sales
- Recent Orders
- State filter
- City filter
- Category filter
- Sub Category filter
- Payment Mode filter
- Order Date filter

## 🖥️ Dashboard

![E-Commerce Sales Dashboard](Screenshots/dashboard.png)

## 🔄 Project Workflow

```text
Raw Dataset
     ↓
SQL Server
     ↓
SQL Analysis
     ↓
Python Analysis
     ↓
Power BI
     ↓
Interactive Dashboard