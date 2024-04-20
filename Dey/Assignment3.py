import pandas 

df = pandas.read_csv('churn_prediction.csv')

print(df.head(10))

print(df.shape)

print(df[['age', 'gender', 'occupation']])

print(df[df['customer_nw_category'] == 3])

print(df[(df['current_balance'] > 5000) & (df['churn'] == 0)])
print(df[(df['age'] >= 30) & (df['age'] <= 40) & (df['occupation'] == 'salaried')])