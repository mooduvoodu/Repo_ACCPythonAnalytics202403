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

multi_group_var2 = (df
                    .groupby 
                    (['gender', 'occupation]) 
                    [['current_month_balance', 'previous_month_balance']]
                              .mean()       
                               )

print(multi_group_var2)


flat= multi_group_var2.reset_index()
print(flat)

print(df.groupby('gender')['occupation'].nunique()0
print(df.groupby('gender')['occupation'].value_counts().reset_index())

display(df.loc[df['current_month_balance'] > 10000.0])

scientist = panda.DataFrame(
  {
    "Name": ["Rosaline Franklin", "William Gosset"],
    "Occupation": ["Chemist", "Statitician"],
    "Born": ["1920-07-25", "1876-06-13"],
    "Died": ["1958-04-16", "1937-10-16"]
    "Age": [37, 61],
  }
)

print(scientists)

scientists = pandas.DataFrame(
  data={
    "Occupation": ["Chemist", "Statitician"]
    "Born": ["1920-07-25", "1876-06-13"],
    "Died": ["1958-04-16", "1937-10-16"]
    "Age": [37, 61],
  },
  index=["Rosaline Franklin", "William Gosset"],
  columns=["Occupation", "Born", "Died", "Age"],
)  

print(scientists)

ages = scientist['Age']
print(ages)

print(ages.mean())

print(ages.min())

print(ages.max())

print(ages.std())

print(ages + ages)

print(ages + 100)

print (ages * 2)


    
