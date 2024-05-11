df = pandas.read_csv('workspaces/Repo_ACCPythonAnalytics202403/classfiles/datasets/churn_prediction.csv')
print(df.groupby('occupation')['current_month_balance'].mean()

grouped_df = df.groupby('occupation')
print(type(grouped_df))

print(grouped_df)

grouped_occupation_df_lifeExp = grouped_df['current_month_balance']
print(type(grouped_occupation_df_lifeExp))

mean_answer = grouped_occupaiton_df_lifeExp.mean()
print(mean_answer)

multi_group_var = df\
.groupby(['gender', 'occupation'])\
.mean()

print(multi_group_var)

multi_group_var2 = (df.groupby(['gender', 'occupation]) [['current_month_balance', 'previous_month_balance']].mean())
