
### Step 1: Define Sample Data

#### Fact Sales Table
- `SaleID`: Unique identifier for each sale
- `CustomerID`: Identifier for the customer
- `DateID`: Identifier for the date of the sale
- `ProductID`: Identifier for the product sold
- `Quantity`: Number of products sold
- `UnitPrice`: Price per unit of the product
- `TotalPrice`: Total price of the sale

#### Dimension Customer Table
- `CustomerID`: Unique identifier for each customer
- `CustomerName`: Name of the customer
- `Segment`: Customer segment
- `Country`: Country of the customer

#### Dimension Date Table
- `DateID`: Unique identifier for each date
- `Date`: Actual date
- `Month`: Month of the year
- `Quarter`: Quarter of the year
- `Year`: Year

### Step 2: Create DataFrames

```python
import pandas as pd
import numpy as np

# Creating the sample data for each table
data_fact_sales = {
    'SaleID': range(1, 21),
    'CustomerID': np.random.choice(range(1, 11), 20),
    'DateID': np.random.choice(range(20230101, 20230121), 20),
    'ProductID': np.random.choice(range(101, 111), 20),
    'Quantity': np.random.randint(1, 10, 20),
    'UnitPrice': np.random.uniform(10.0, 100.0, 20),
}
data_fact_sales['TotalPrice'] = np.array(data_fact_sales['Quantity']) * np.array(data_fact_sales['UnitPrice'])

data_dim_customer = {
    'CustomerID': range(1, 11),
    'CustomerName': [f'Customer{i}' for i in range(1, 11)],
    'Segment': np.random.choice(['Corporate', 'Home Office', 'Consumer'], 10),
    'Country': np.random.choice(['USA', 'Canada', 'Mexico'], 10)
}

data_dim_date = {
    'DateID': range(20230101, 20230121),
    'Date': pd.date_range(start='2023-01-01', periods=20, freq='D'),
    'Month': ['January'] * 20,
    'Quarter': ['Q1'] * 20,
    'Year': [2023] * 20
}

# Converting dictionaries to DataFrames
df_sales = pd.DataFrame(data_fact_sales)
df_customers = pd.DataFrame(data_dim_customer)
df_dates = pd.DataFrame(data_dim_date)

# Display the DataFrames to confirm creation
df_sales.head(), df_customers.head(), df_dates.head()
```

### Step 3: Excercise Instructions


1. **Basic Inner Join**: Join sales data with customer data to see the customer details for each sale.
2. **Left Outer Join**: Show all sales, including customer details, even if the customer details are missing.
3. **Right Outer Join**: Show all customers and their sales, including those who have not made any sales.
4. **Full Outer Join**: Combine sales and customer information, showing all records from both even if there are no matches.
5. **Cross Join**: Generate a combination of every customer with every product.
6. **Group By**: Aggregate sales data to calculate total sales per customer.
7. **Summarizing Data**: Find the total, average, minimum, and maximum sale amount by product.
8. **Window Function - Rank**: Rank customers based on their total sales.
9. **Window Function - Running Total**: Calculate a running total of sales over a period.
10. **Conditional Aggregations**: Calculate total sales for each country where sales are above a certain threshold.
11. **Pivot Table**: Create a pivot table showing total sales by month and by segment.
12. **Time Series Analysis**: Analyze sales trends over the date range.
13. **Merge with Overlapping Columns**: Using different key columns to merge two datasets.
14. **Concatenate Data Vertically**: Combine sales data of different periods.
15. **Filtering on Joins**: Filter sales based on a specific customer attribute.
16. **Multi-level Group By**: Group by both customer and product to find total sales.
17. **Complex Conditions**: Filter sales where the total sale amount is above average.
18. **Handling Missing Data**: Identify and handle missing values in the sales data.
19. **Deduplication**: Remove duplicate entries in customer data.
20. **Custom Calculations**: Calculate profit margins assuming a fixed cost per unit sold.

