import pandas
import datetime

df  = pandas.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/classfiles/datasets/churn_prediction.csv')

#vector work on mismatched series (called broadcasting)
#lined on by index lable
v1 = pandas.Series(range(1,10))
v2 = pandas.Series(range(1,5))
print(v1)

v3 = v1 + v2
print(v3)

# Data Frame parts review

print(df.index)

print(df.columns)

print(df.values)

# Boolean review , Refer to book subsetting table.

print(df.loc[df['age'] > df['age'].mean()])

#Broadcasting with entire data frame

middlerow = (len(df) // 2)

first_half = df[:middlerow]
second_half = df[((len(df) // 2) + 1): ] 

print(first_half)
print(second_half)

display(first_half * 2)


## more transforms
## adding columns

print(df.dtypes)

##get object turned to datetime format

# format the 'Born' column as a datetime
lastT_datetime = pandas.to_datetime(df['last_transaction'], format='%Y-%m-%d')
print(lastT_datetime)

#bring in new column
df['lastT_dt'] = lastT_datetime

display(df)

print(df.dtypes)

##multiple column add
##scientists['born_dt'], scientists['died_dt'] = (
##  born_datetime,
##  died_datetime
##) 

## easy column data change

df['vintage'] = df['vintage'] - 10000
display(df)

## index influence on order, data view show

random1 = df['vintage'].sample(frac=1, random_state=42)

df['vintage'] = random1
display(df)

df['vintage'] = (
df['vintage']
  .sample(frac=1, random_state=42)
  .values # remove the index so it doesn't auto align the values
)

display(df['vintage'])


##  .assign()    to modify columns
## change existing column and add new one

df = df.assign(
    newcol1 = 'sometext',
    age = df['age'] + 100
)

display(df)

##dropping column/Values

df_droppedCol = df.drop(['newcol1'], axis="columns")
print(df_droppedCol)


## export to CSV
df_droppedCol

df_droppedCol.to_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/churn_prediction_output.csv', index=False)
df_droppedCol.to_
 


print(df['customer_nw_category'] == 3)