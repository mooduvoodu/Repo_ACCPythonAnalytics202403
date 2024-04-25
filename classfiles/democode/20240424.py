## demo for Chp 4,5

import pandas
import datetime

df  = pandas.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/classfiles/datasets/supermarket_sales - Sheet1.csv')

print(df.dtypes)

##.melt()   Pivot and UnPivot slide overview
# 
#  

#string maniplution
# The  code demonstrates different string methods such as converting to 
# lowercase/uppercase/title case, finding the length of strings, splitting strings, 
# replacing parts of strings, checking for the presence of a substring, extracting 
# specific parts of a string, stripping whitespace, and finding the position of a 
# substring. These methods are useful for data cleaning, preparation, and analysis in pandas.

df['Product line lower'] = df['Product line'].str.lower()

df['Product line upper'] = df['Product line'].str.upper()

df['Product line title'] = df['Product line'].str.title()

df['Product line length'] = df['Product line'].str.len()

df['Date split'] = df['Date'].str.split('/')

df['City replace'] = df['City'].str.replace('Yangon', 'YGN')

df['Contains Health'] = df['Product line'].str.contains('Health')

df['First letter of Gender'] = df['Gender'].str.extract(r'(^\w)')

df['Payment stripped'] = df['Payment'].str.strip()

df['Find Ewallet'] = df['Payment'].str.find('Ewallet')

#Datetime common transformations
df['Date'] = pandas.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year

df['Month'] = df['Date'].dt.month

df['Day'] = df['Date'].dt.day

df['DayOfWeek'] = df['Date'].dt.dayofweek

df['DayName'] = df['Date'].dt.day_name()

df['WeekOfYear'] = df['Date'].dt.isocalendar().week

df['Quarter'] = df['Date'].dt.quarter

#df.set_index('Date', inplace=True)
display(df)


#Apply Functions to transform df data

#simple functions
def my_exp(x, e):
  return x ** e

cubed = my_exp(2, 3)
print(cubed)


ex = df['Total'].apply(my_exp, e=2)
print(ex)

#full data frame

df_reduced = df.loc[0:2,['Invoice ID','Total']]
print(df_reduced)

def print_me(x):
  print(x)

df_reduced.apply(print_me, axis=0)  #Col wise


df_reduced.apply(print_me, axis=1)  #row wise
 
def avg_3(x, y, z):
  return (x + y + z) / 3

 # will cause an error
print(df_reduced.apply(avg_3))
 

def avg_3_apply(col):
  """The avg_3 function but apply compatible
  by taking in all the values as the first argument
  and parsing out the values within the function
  """
  x = col[0]
  y = col[1]
  z = col[2]
  return (x + y + z) / 3 

print(df_reduced.apply(avg_3_apply))


 
