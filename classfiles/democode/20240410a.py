import pandas
import datetime


df  = pandas.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/classfiles/datasets/churn_prediction.csv')

# For each year in our data, what was the average life expectancy?
# To answer this question, we need to:
# 1. split our data into parts by year
# 2. get the 'occupation' column
# 3. calculate the mean
print(df.groupby('occupation')['current_month_balance'].mean())



# create grouped object by occupation 
grouped_df = df.groupby('occupation')
print(type(grouped_df))


# what if we just look at grouped
print(grouped_df)

grouped_occupation_df_lifeExp = grouped_df['current_month_balance']
print(type(grouped_occupation_df_lifeExp))


mean_answer = grouped_occupation_df_lifeExp.mean()
print(mean_answer)

## group by more than 1 column

# the backslash allows us to break up 1 long line of python code
# into multiple lines
# df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
# is the same as
multi_group_var = df\
  .groupby(['gender', 'occupation'])\
  [['current_month_balance', 'previous_month_balance']]\
  .mean() 

print(multi_group_var)


# we can also wrap the entire statement
# around round parentheses
# with each .method() on a new line
# this is the preferred style for writing "method chaining"
multi_group_var2 = (
  df
  .groupby(['gender', 'occupation'])
  [['current_month_balance', 'previous_month_balance']]
  .mean()
)

print(multi_group_var2)
 
flat = multi_group_var2.reset_index()
print(flat)

# use the nunique (number unique)
# to calculate the number of unique values in a series
print(df.groupby('gender')['occupation'].nunique())
print(df.groupby('gender')['occupation'].value_counts().reset_index())



#Boolean Subsetting

#display(df.loc[df['current_month_balance'] > 10000.0])


#Creating ad hoc dataframes

scientists = pandas.DataFrame(
  {
    "Name": ["Rosaline Franklin", "William Gosset"],
    "Occupation": ["Chemist", "Statistician"],
    "Born": ["1920-07-25", "1876-06-13"],
    "Died": ["1958-04-16", "1937-10-16"],
    "Age": [37, 61],
  }
)

print(scientists)

scientists = pandas.DataFrame(
  data={
    "Occupation": ["Chemist", "Statistician"],
    "Born": ["1920-07-25", "1876-06-13"],
    "Died": ["1958-04-16", "1937-10-16"],
    "Age": [37, 61],
  },
  index=["Rosaline Franklin", "William Gosset"],
  columns=["Occupation", "Born", "Died", "Age"],
)
print(scientists)

# get the 'Age' column
ages = scientists['Age']
print(ages)

# calculate the mean
print(ages.mean()) 
# calculate the minimum
print(ages.min())
# calculate the maximum
print(ages.max())
# calculate the standard deviation
print(ages.std())


#vectors are aligned and will have calculations work against each element, same length

print(ages + ages)

print(ages + 100)

print(ages * 2)
 

