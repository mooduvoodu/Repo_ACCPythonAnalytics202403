

### Exercise Set:

Using the following 2 tables for Sales and Customers
**Starter Code:**
```python
import pandas as pd

# Example sales DataFrame
data_sales = {
    'customer_id': [1, 2, 1, 3],
    'sales_amount': [100, 200, 150, 400]
}
sales = pd.DataFrame(data_sales)

# Example customers DataFrame
data_customers = {
    'customer_id': [1, 2, 4],
    'customer_name': ['Alice', 'Bob', 'Charlie']
}
customers = pd.DataFrame(data_customers)
```

#### Exercise 1: Basic Data Viewing
Display the first three rows of both the `sales` and `customers` DataFrames.

#### Exercise 2: Cross Join
Perform a cross join between the `sales` and `customers` DataFrames. Display the resulting DataFrame.

#### Exercise 3: Inner Join
Perform an inner join between the `sales` and `customers` DataFrames on the `customer_id` column. Display the resulting DataFrame.

#### Exercise 4: Right Outer Join
Perform a right outer join between the `sales` and `customers` DataFrames. Display the resulting DataFrame and identify any customer records that do not have corresponding sales.

#### Exercise 5: Left Outer Join
Perform a left outer join between the `sales` and `customers` DataFrames. Display the resulting DataFrame and identify any sales records that do not have corresponding customer details.

#### Exercise 6: Full Outer Join
Perform a full outer join between the `sales` and `customers` DataFrames. Display the resulting DataFrame and identify records from both `sales` and `customers` that did not match with the other table.

#### Exercise 7: Summarize Sales Data
Using the result from the inner join in Exercise 3, calculate the total sales per customer. Display a DataFrame that includes the customer's name and their total sales.

#### Exercise 8: Compute Sales Tax
After performing an inner join between the `sales` and `customers` DataFrames, add a new column to the resulting DataFrame that calculates the tax (assuming a flat rate of 10%) on the sales amount.
