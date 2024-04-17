
### Solution Code

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('churn_prediction.csv')

# Solutions
# 1. Basic Information Extraction
print(df.head(10))
print(df.shape)

# 2. Column-based Subsetting
print(df[['age', 'gender', 'occupation']])

# 3. Row-based Subsetting
print(df[df['customer_nw_category'] == 3])

# 4. Conditional Subsetting
print(df[(df['current_balance'] > 5000) & (df['churn'] == 0)])

# 5. Multiple Conditions in Subsetting
print(df[(df['age'] >= 30) & (df['age'] <= 40) & (df['occupation'] == 'salaried')])

# 6. Column Creation
df['balance_category'] = pd.cut(df['current_balance'], bins=[-float('inf'), 3000, 7000, float('inf')], labels=['Low', 'Medium', 'High'])
print(df[['current_balance', 'balance_category']])

# 7. Grouped Calculations
print(df.groupby('gender')['current_balance'].mean())

# 8. Aggregated Grouped Calculations
print(df.groupby('occupation').agg({'current_month_credit': 'sum', 'previous_month_balance': 'mean'}))

# 9. Advanced Grouping
print(df[df['customer_nw_category'] == 2].groupby('occupation').agg({'age': 'max', 'current_balance': 'min'}))

# 10. Date Manipulation
df['last_transaction'] = pd.to_datetime(df['last_transaction'])
df['month_of_last_transaction'] = df['last_transaction'].dt.month
print(df[['last_transaction', 'month_of_last_transaction']])
```
