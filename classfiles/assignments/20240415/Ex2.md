Based on the schema of the `churn_prediction.csv` file, here are 10 exercises for a Python analytics class focusing on Pandas dataframes, boolean subsetting, grouped and aggregate calculations, and aggregate analysis. The sample solutions are provided in the solution file in the same folder. Your solutions can be different.

### Exercise 1: Basic Data Overview
**Task:** Load the `churn_prediction.csv` dataset using Pandas and display the first 10 rows. Also, print the shape of the DataFrame.

### Exercise 2: Data Filtering
**Task:** From the dataset, select only those customers who are self-employed (`occupation` column) and have a current balance of more than 5000. Display the first 5 rows of this subset.

### Exercise 3: Gender-based Analysis
**Task:** Find the average `current_balance` for each gender. Handle missing values in the `gender` column appropriately.

### Exercise 4: Age Group Analysis
**Task:** Create a new column `age_group` categorizing customers into 'Young' (age <= 30), 'Middle-Aged' (30 < age <= 60), and 'Senior' (age > 60). Display the first 5 rows after adding this column.

### Exercise 5: Aggregate Analysis on Age Group
**Task:** For each `age_group`, find the average `current_balance` and the total number of customers who have churned (`churn` column).

### Exercise 6: City-wise Customer Count
**Task:** Count the number of customers in each city. Display the top 5 cities with the highest number of customers.

### Exercise 7: High-Value Customers in Occupations
**Task:** Identify the top 3 occupations that have the highest average `customer_nw_category`.

### Exercise 8: Monthly Balance Comparison
**Task:** Calculate the difference between `current_month_balance` and `previous_month_balance` for each customer. Find out how many customers have a positive difference.

### Exercise 9: Credit-Debit Analysis
**Task:** For each customer, calculate the ratio of `current_month_credit` to `current_month_debit`. Exclude customers with zero debit to avoid division by zero errors. Find the average of these ratios.

### Exercise 10: Last Transaction Analysis
**Task:** Convert the `last_transaction` column to datetime format. Find out how many customers made their last transaction in the year 2019.
