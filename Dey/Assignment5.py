import pandas as pd
import numpy as np

# Creating the sample data for each table
data_fact_sales = {
    'SaleID': range(1, 21),
    'CustomerID': np.random.choice(range(1, 11), 20),
    'DateID': np.random.choice(range(20230101, 20230121), 20),
    'ProductID': np.random.choice(range(101, 111), 20),
    'Quantity': np.random.randint(1, 10, 20),
    'UnitPrice': np.random.uniform(10.0, 100.0, 20),
}
data_fact_sales['TotalPrice'] = np.array(data_fact_sales['Quantity']) * np.array(data_fact_sales['UnitPrice'])

data_dim_customer = {
    'CustomerID': range(1, 11),
    'CustomerName': [f'Customer{i}' for i in range(1, 11)],
    'Segment': np.random.choice(['Corporate', 'Home Office', 'Consumer'], 10),
    'Country': np.random.choice(['USA', 'Canada', 'Mexico'], 10)
}

data_dim_date = {
    'DateID': range(20230101, 20230121),
    'Date': pd.date_range(start='2023-01-01', periods=20, freq='D'),
    'Month': ['January'] * 20,
    'Quarter': ['Q1'] * 20,
    'Year': [2023] * 20
}

# Converting dictionaries to DataFrames
df_sales = pd.DataFrame(data_fact_sales)
df_customers = pd.DataFrame(data_dim_customer)
df_dates = pd.DataFrame(data_dim_date)

# Display the DataFrames to confirm creation
df_sales.head(), df_customers.head(), df_dates.head()

#1 Basic inner join
sales_with_customers = pd.merge(df_sales, df_customers, on='CustomerID', how='inner')
display(sales_with_customers)

#2 Left Outer Join
sales_with_customers_left = pd.merge(df_sales, df_customers, on='CustomerID', how='left')
display(sales_with_customers_left)

#3 Right Outer Join
customers_with_sales_right = pd.merge(df_sales, df_customers, on='CustomerID', how='right')
display(customers_with_sales_right)

#4 Full Outer Join
full_outer_join = pd.merge(df_sales, df_customers, on='CustomerID', how='outer')
display(full_outer_join)

#5 Cross Join
customers_products_cross = df_customers.assign(key=1).merge(df_sales.assign(key=1), on='key').drop('key', axis=1)
display(customers_products_cross)

#6 Group By
total_sales_per_customer = df_sales.groupby('CustomerID').agg(Total_Sales=pd.NamedAgg(column='TotalPrice', aggfunc='sum'))
display(total_sales_per_customer)

#7 Summarizing Data
summary_stats = df_sales.groupby('ProductID')['TotalPrice'].agg(['sum', 'mean', 'min', 'max'])
display(summary_stats)

#8 Window Function - Rank
df_sales['Rank'] = df_sales.groupby('CustomerID')['TotalPrice'].rank(method='dense', ascending=False)
display(df_sales['Rank']) 

#9 Window Function - Running Total
df_sales['Running_Total'] = df_sales.sort_values('DateID').groupby('CustomerID')['TotalPrice'].cumsum()
display(df_sales['Running_Total'])

#10 Conditional Aggregation
sales_above_threshold = df_sales[df_sales['TotalPrice'] > 50].groupby('CustomerID').agg(Total_Sales=pd.NamedAgg(column='TotalPrice', aggfunc='sum'))
display(sales_above_threshold)

#11	Pivot Table
pivot_sales = pd.pivot_table(df_sales, values='TotalPrice', index='DateID', columns='CustomerID', aggfunc='sum', fill_value=0)

display(pivot_sales)

#12	Time Series Analysis
df_sales['Month'] = pd.to_datetime(df_sales['DateID'], format='%Y%m%d').dt.month
time_series_analysis = df_sales.groupby('Month')['TotalPrice'].sum()
display(time_series_analysis)

#13 Merge with Overlapping Columns
sales_customers_merged = pd.merge(df_sales, df_customers[['CustomerID', 'Segment']], on='CustomerID')

#14 Concatenate Data Vertically
combined_sales = pd.concat([df_sales, df_sales_previous])

#15	Filtering on Joins
filtered_join = pd.merge(df_sales, df_customers[df_customers['Country'] == 'USA'], on='CustomerID')

#16 Multi-level Group By
multilevel_groupby = df_sales.groupby(['CustomerID', 'ProductID']).agg(Total_Sales=pd.NamedAgg(column='TotalPrice', aggfunc='sum'))


#17	Complex Conditions
average_sale = df_sales['TotalPrice'].mean()
sales_above_average = df_sales[df_sales['TotalPrice'] > average_sale]
display(sales_above_average)

#18 Handling Missing Data
df_sales_filled = df_sales.fillna({'UnitPrice': df_sales['UnitPrice'].mean()})

#19	Deduplication
df_customers_deduplicated = df_customers.drop_duplicates()

#20	Custom Calculations
df_sales['Profit'] = df_sales['TotalPrice'] - (df_sales['Quantity'] * 5)  # Assuming cost per unit is 5
