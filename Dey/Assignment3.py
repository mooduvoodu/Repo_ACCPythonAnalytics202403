import pandas 
import datetime

df = pandas.read_csv('churn_prediction.csv')

print(df.head(10))

print(df.shape)

print(df[['age', 'gender', 'occupation']])

print(df[df['customer_nw_category'] == 3])

print(df[(df['current_balance'] > 5000) & (df['churn'] == 0)])

print(df[(df['age'] >= 30) & (df['age'] <= 40) & (df['occupation'] == 'salaried')])

df['balance_category'] = pandas.cut(df['current_balance'], bins=[-float('inf'), 3000, 7000, float('inf')], labels=['Low', 'Medium', 'High'])

print(df[['current_balance', 'balance_category']])

print(df.groupby('gender')['current_balance'].mean())

print(df.groupby('occupation').agg({'current_month_credit': 'sum', 'previous_month_balance': 'mean'}))

print(df[df['customer_nw_category'] == 2].groupby('occupation').agg({'age': 'max', 'current_balance': 'min'}))

df['last_transaction'] = pandas.to_datetime(df['last_transaction'])

df['month_of_last_transaction'] = df['last_transaction'].dt.month

print(df[['last_transaction', 'month_of_last_transaction']])



