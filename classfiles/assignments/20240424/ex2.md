Using the same sales and customer data sets

### Exercise Set:

#### Exercise 1: Using `apply()` to Calculate Discounts
Calculate a 15% discount on the `sales_amount` for each sale in the `sales` DataFrame and add it as a new column named `discount_amount`. Use the `apply()` function to apply this calculation.

#### Exercise 2: Customer Status Tag with `apply()`
Create a new column `customer_status` in the `customers` DataFrame that tags each customer as "Priority" if their name starts with 'A' and "Standard" otherwise. Use the `apply()` function to perform this operation.

#### Exercise 3: Concatenate `sales` and `customers`
Create a new DataFrame by concatenating the `sales` and `customers` DataFrames vertically, despite them having different schemas. Display the resulting DataFrame.

#### Exercise 4: Combining Adjusted Sales Data
After performing Exercise 1, concatenate the original `sales` DataFrame with the adjusted sales DataFrame (which includes the `discount_amount`) horizontally to compare the original and discounted sales amounts.

#### Exercise 5: Analysis of Concatenated Data
Using the result from Exercise 3, analyze the concatenated DataFrame to identify how many rows pertain to sales data and how many pertain to customer data. Use the `isnull()` function combined with `apply()` for this analysis.
