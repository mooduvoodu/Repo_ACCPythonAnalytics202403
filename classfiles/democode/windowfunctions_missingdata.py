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

# Check for missing values in each column
missing_data = df_sales.isnull().sum()  # Output the sum of missing values per column

# Fill missing numeric values with the column's mean
df_sales['UnitPrice'] = df_sales['UnitPrice'].fillna(df_sales['UnitPrice'].mean())  # Use mean to fill nulls in UnitPrice

# Fill missing categorical data with the mode (most frequent value)
df_customers['Country'] = df_customers['Country'].fillna(df_customers['Country'].mode()[0])  # Fill with the most common country

# Remove rows where specific critical columns have missing values
cleaned_sales = df_sales.dropna(subset=['CustomerID', 'TotalPrice'])  # Drop rows with nulls in 'CustomerID' or 'TotalPrice'

# Apply linear interpolation to fill missing numeric values
df_sales['UnitPrice'] = df_sales['UnitPrice'].interpolate()  # Linear interpolation of 'UnitPrice'

# Use forward fill to propagate last observed non-null value
df_sales['Country'] = df_sales['Country'].fillna(method='ffill')  # Forward fill 'Country' to replace nulls

# Use backward fill to use next non-null value to fill current null
df_sales['Country'] = df_sales['Country'].fillna(method='bfill')  # Backward fill 'Country' for missing values

# Replace specific placeholder values that represent missing data
df_sales['UnitPrice'] = df_sales['UnitPrice'].replace(0, np.nan)  # Assume 0 as placeholder for missing, replace with NaN

# Fill missing values conditionally based on other column values
df_sales.loc[df_sales['Quantity'] == 0, 'UnitPrice'] = df_sales['UnitPrice'].fillna(50)  # Set UnitPrice to 50 if Quantity is 0

# Check multiple columns for missing values at once
multi_null_check = df_sales[['CustomerID', 'ProductID']].isnull().any(axis=1)  # True if any specified columns have nulls


#More Window Functions
# Assign sequential numbers to each row within each group defined by 'CustomerID'
df_sales['Row_Number'] = df_sales.groupby('CustomerID').cumcount() + 1  # Sequential row number within each customer group

# Calculate cumulative total of 'TotalPrice' within each 'CustomerID' group
df_sales['Running_Total'] = df_sales.groupby('CustomerID')['TotalPrice'].cumsum()  # Running total of sales per customer

# Calculate a moving average of 'TotalPrice' within each customer group
df_sales['Moving_Avg'] = df_sales.groupby('CustomerID')['TotalPrice'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())

# Rank 'TotalPrice' within each 'CustomerID' group, with ties sharing the same rank
df_sales['Rank'] = df_sales.groupby('CustomerID')['TotalPrice'].rank(method='average')

# Dense rank 'TotalPrice' within each 'CustomerID' group, without gaps in rank values
df_sales['Dense_Rank'] = df_sales.groupby('CustomerID')['TotalPrice'].rank(method='dense')

# Calculate percentile rank within each 'CustomerID' group for 'TotalPrice'
df_sales['Percent_Rank'] = df_sales.groupby('CustomerID')['TotalPrice'].rank(pct=True)

# Access the 'TotalPrice' of the previous row within the same 'CustomerID' group
df_sales['Previous_Sale'] = df_sales.groupby('CustomerID')['TotalPrice'].shift(1)  # Get previous sale price

# Access the 'TotalPrice' of the next row within the same 'CustomerID' group
df_sales['Next_Sale'] = df_sales.groupby('CustomerID')['TotalPrice'].shift(-1)  # Get next sale price

# Track the cumulative maximum of 'TotalPrice' reached so far within each customer group
df_sales['Cumulative_Max'] = df_sales.groupby('CustomerID')['TotalPrice'].cummax()  # Cumulative max sales per customer

# Retrieve the first 'TotalPrice' encountered in each customer group
df_sales['First_Sale'] = df_sales.groupby('CustomerID')['TotalPrice'].transform('first')  # First sale amount per customer