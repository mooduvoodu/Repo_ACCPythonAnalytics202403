import pandas 

df = pandas.read_csv('churn_prediction.csv')

print(df.head(10))

print(df.shape)

print(df[['age', 'gender', 'occupation']])

print(df[df['customer_nw_category'] == 3])
