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
