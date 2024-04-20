import pandas as pd

DF=pd.read_csv('churn_prediction.csv')
               
print(DF.head(10))
print(DF.shape)
subset=DF[(DF['current_balance'] > 5000) &( DF['occupation'] == 'self_employed')]
print(subset.head(5))

