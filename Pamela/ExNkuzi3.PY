### Solutions

1. **Basic Data Overview**
   ```python
   import pandas as pd
   data = pd.read_csv('churn_prediction.csv')
   print(data.head(10))
   print(data.shape)
   ```

2. **Data Filtering**
   ```python
   subset = data[(data['occupation'] == 'self_employed') & (data['current_balance'] > 5000)]
   print(subset.head(5))
   ```

3. **Gender-based Analysis**
   ```python
   avg_balance = data.groupby('gender')['current_balance'].mean()
   print(avg_balance)
   ```

4. **Age Group Analysis**
   ```python
   data['age_group'] = pd.cut(data['age'], bins=[0, 30, 60, float('inf')], labels=['Young', 'Middle-Aged', 'Senior'])
   print(data.head(5))
   ```

5. **Aggregate Analysis on Age Group**
   ```python
   age_group_analysis = data.groupby('age_group').agg({'current_balance': 'mean', 'churn': 'sum'})
   print(age_group_analysis)
   ```

6. **City-wise Customer Count**
   ```python
   city_count = data['city'].value_counts().head(5)
   print(city_count)
   ```

7. **High-Value Customers in Occupations**
   ```python
   top_occupations = data.groupby('occupation')['customer_nw_category'].mean().nlargest(3)
   print(top_occupations)
   ```

8. **Monthly Balance Comparison**
   ```python
   balance_diff = (data['current_month_balance'] - data['previous_month_balance']) > 0
   print(balance_diff.sum())
   ```

9. **Credit-Debit Analysis**
   ```python
   valid_data = data[data['current_month_debit'] != 0]
   ratio = (valid_data['current_month_credit'] / valid_data['current_month_debit']).mean()
   print(ratio)
   ```

10. **Last Transaction Analysis**
    ```python
    data['last_transaction'] = pd.to_datetime(data['last_transaction'])
    transactions_2019 = data['last_transaction'].dt.year == 2019
    print(transactions_2019.sum())
    ``` 
