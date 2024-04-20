import pandas as pd
import datetime

DF=pd.read_csv('churn_prediction.csv')
               
print(DF.head(10))
print(DF.shape)
subset=DF[(DF['current_balance'] > 5000) &( DF['occupation'] == 'self_employed')]
print(subset.head(5))

avg_balance = DF.groupby('gender')['current_balance'].mean()
print(avg_balance)

DF['age_group'] = pd.cut(DF['age'], bins=[0, 30, 60, float('inf')], labels=['Young', 'Middle-Aged', 'Senior'])
print(DF.head(5))

age_group_analysis =DF.groupby('age_group').agg({'current_balance': 'mean', 'churn': 'sum'})
print(age_group_analysis)


city_count = DF['city'].value_counts()
print(city_count.head(5))

top_occupations = DF.groupby('occupation')['customer_nw_category'].mean()
print (top_occupations.nlargest(3))

balance_diff =(DF['current_month_balance'] - DF['previous_month_balance']) > 0
print(balance_diff.value_counts()) 

valid_data = DF[DF['current_month_debit'] != 0]
ratio = (valid_data['current_month_credit'] / valid_data['current_month_debit']).mean()
print(ratio)

DF['last_transaction'] = pd.to_datetime(DF['last_transaction'])
transactions_2019 = DF['last_transaction'].dt.year == 2019
print(transactions_2019.value_counts())
