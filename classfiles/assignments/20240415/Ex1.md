Based on the structure of the `churn_prediction.csv` dataset, here are 10 exercises focusing on Pandas dataframes, including subsetting, slicing, grouping, and aggregate calculations. The sample solutions are provided in the solution file in the same folder. Your solutions can be different.

### Exercises

1. **Basic Information Extraction:**
   - Print the first 10 rows of the dataset.
   - Display the number of rows and columns in the dataset.

2. **Column-based Subsetting:**
   - Extract and display only the `age`, `gender`, and `occupation` columns from the dataset.

3. **Row-based Subsetting:**
   - Select and display the rows where the `customer_nw_category` is 3.

4. **Conditional Subsetting:**
   - Find all rows where the `current_balance` is greater than 5000 and the `churn` is 0.

5. **Multiple Conditions in Subsetting:**
   - Retrieve and display rows where `age` is between 30 and 40, and `occupation` is 'salaried'.

6. **Column Creation:**
   - Create a new column `balance_category` based on `current_balance`. Assign 'Low' if `current_balance` <= 3000, 'Medium' if it's between 3000 and 7000, and 'High' otherwise.

7. **Grouped Calculations:**
   - Group the dataset by `gender` and calculate the average `current_balance` for each gender.

8. **Aggregated Grouped Calculations:**
   - Group the dataset by `occupation` and calculate the sum of `current_month_credit` and the average of `previous_month_balance` for each occupation.

9. **Advanced Grouping:**
   - For customers with `customer_nw_category` as 2, group by `occupation` and find the maximum `age` and minimum `current_balance`.

10. **Date Manipulation:**
    - Convert the `last_transaction` column to datetime format and create a new column `month_of_last_transaction` indicating the month of the last transaction.
