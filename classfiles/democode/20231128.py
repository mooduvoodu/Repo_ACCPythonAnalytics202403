## demo code to complement Pandas book. Chp 1, 2

## understand the data from the dataset
## Aggregate Analysis - focus on Group By and Aggregate Functions

import pandas
import datetime


df  = pandas.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/churn_prediction.csv')

df2 = pandas.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/3_stephen_curry_shot_chart_2023.csv')

print(df)


df.head()


print(type(df))
print(df.shape)   # attribute

print(df.columns)

# get the dtype of each column
print(df.dtypes)

 # get more information about our data
print(df.info())

## SQL logical processing order Review
## FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY

# just get the country column and save it to its own variable, series dtype 
## sometime called a vector
age_df = df['age']

# show the first 5 observations
print(age_df.head())

# show the last 5 observations
print(age_df.tail())

# Multiple Columns , Dataframe dtype
subset = df[['age', 'gender', 'customer_id']]
display(subset)


#dot notation, #carefull on name collision and names with special characters

print(df.age)


# name collision 
df.shape

 # subset rows ( equivalant SQL WHERE)
 # .loc[]  &  .iloc[]

 # get the first row
# python counts from 0
print(df.loc[0])

 # get the 100th row
# python counts from 0
print(df.loc[99])

## multiple rows

display(df.loc[[0, 99, 999]])

## subset rows by number

# get the 2nd row
print(df.iloc[1])

 ## get the 100th row
print(df.iloc[99])

## get the first, 100th, and 1000th row
print(df.iloc[[0, 99, 999]])


## subset rows and columns
# df.loc[[rows], [columns]] or df.iloc[[rows], [columns]].

# subset columns with loc
# note the position of the colon
# it is used to select all rows
subset = df.loc[:, ['customer_id', 'gender']]
display(subset)

 # subset columns with iloc
# iloc will allow us to use integers
# -1 will select the last column
subset = df.iloc[:, [2, 4, -1]]
display(subset)

 ##subset with range , similar to slicing

 # create a range of integers from 0 - 4 inclusive
small_range = list(range(5))
print(small_range)

# subset the dataframe with the range
subset = df.iloc[:, small_range]
print(subset)

# create a range from 3 - 5 inclusive
small_range = list(range(3, 6))
print(small_range)

subset = df.iloc[:, small_range]
print(subset)

# create a range from 0 - 5 inclusive, every other integer
small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)

 
small_range = list(range(3))
subset = df.iloc[:, small_range]
print(subset)
 
# slice the first 3 columns
subset = df.iloc[:, :3]
print(subset)

small_range = list(range(3, 6))
subset = df.iloc[:, small_range]
print(subset)

# slice columns 3 to 5 inclusive
subset = df.iloc[:, 3:6]
print(subset)

 # slice every other columns
subset = df.iloc[:, 0:6:2]
print(subset)

# get the 1st, 100th, and 1000th rows
# from the 1st, 4th, and 6th column
# note the columns we are hoping to get are:

print(df.iloc[[0, 99, 999], [0, 3, 5]])

# if we use the column names directly,
# it makes the code a bit easier to read
# note now we have to use loc, instead of iloc
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

 

 


 
 
