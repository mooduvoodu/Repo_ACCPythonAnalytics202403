import pandas as pd

# Re-reading the provided CSV files using the correct delimiter '|'
order_header_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/sales/orderheader.csv', delimiter='|')
order_details_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/sales/orderdetails.csv', delimiter='|')
customers_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/sales/customers.csv', delimiter='|', encoding='ISO-8859-1')

# Preparing dataframes for joins using only the 'join' method
# For 'join' to work properly, the joining columns must be the index in at least one of the dataframes
# Setting 'CustomerID' as index for customers_df and 'SalesOrderID' for order_details_df
customers_df.set_index('CustomerID', inplace=True)
order_details_df.set_index('SalesOrderID', inplace=True)

# For cross join, we create a temporary key column in each dataframe because join does not directly support cross joins
order_header_df['key'] = 1
customers_df['key'] = 1

# Cross Join
cross_join_df = order_header_df.join(customers_df, on='key', how='outer', lsuffix='_header', rsuffix='_customer').drop(['key_header', 'key_customer'], axis=1)

# Resetting index to enable other joins
customers_df.reset_index(inplace=True)

# Inner Join
# For inner join, setting 'CustomerID' as index for both dataframes
order_header_df.set_index('CustomerID', inplace=True)
customers_df.set_index('CustomerID', inplace=True)
inner_join_df = order_header_df.join(customers_df, how='inner', lsuffix='_header', rsuffix='_customer')

# Left Outer Join
# Resetting index for order_header_df to demonstrate left join
order_header_df.reset_index(inplace=True)
order_header_df.set_index('CustomerID', inplace=True)
left_outer_join_df = order_header_df.join(customers_df, how='left', lsuffix='_header', rsuffix='_customer')

# Right Outer Join
# Resetting index for customers_df to demonstrate right join
customers_df.reset_index(inplace=True)
customers_df.set_index('CustomerID', inplace=True)
right_outer_join_df = order_header_df.join(customers_df, how='right', lsuffix='_header', rsuffix='_customer')

# Full Outer Join
full_outer_join_df = order_header_df.join(customers_df, how='outer', lsuffix='_header', rsuffix='_customer')

# Resetting indices to original for all dataframes
order_header_df.reset_index(inplace=True)
customers_df.reset_index(inplace=True)
order_details_df.reset_index(inplace=True)

# Displaying the first few rows of each join
{
    "Cross Join": cross_join_df.head(),
    "Inner Join": inner_join_df.head(),
    "Left Outer Join": left_outer_join_df.head(),
    "Right Outer Join": right_outer_join_df.head(),
    "Full Outer Join": full_outer_join_df.head()
}

# advanced aggregation

df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/sales/orderheader.csv', delimiter='|')

# Perform aggregations using .agg() method
aggregated_data = df.groupby('Status').agg(
    TotalSubTotal=('SubTotal', 'sum'),
    TotalTaxAmt=('TaxAmt', 'sum'),
    TotalFreight=('Freight', 'sum'),
    AverageTotalDue=('TotalDue', 'mean')
)

aggregated_data.reset_index(inplace=True)
aggregated_data.head()


# Define custom aggregate functions

def range_agg(series):
    """Calculate the range of a series."""
    return series.max() - series.min()

def median_agg(series):
    """Calculate the median of a series."""
    return series.median()

def percentile_90(series):
    """Calculate the 90th percentile of a series."""
    return series.quantile(0.90)

# Applying custom aggregate functions
custom_aggregated_data = df.groupby('Status').agg(
    SubTotalRange=('SubTotal', range_agg),
    TaxAmtMedian=('TaxAmt', median_agg),
    Freight90thPercentile=('Freight', percentile_90)
)

custom_aggregated_data.reset_index(inplace=True)
display(custom_aggregated_data)


#Transform - does not reduce data like aggregates

# Aggregate the data
grouped_data = df.groupby('Status').agg(
    TotalSubTotal=('SubTotal', 'sum'),
    TotalTaxAmt=('TaxAmt', 'sum'),
    TotalFreight=('Freight', 'sum')
)

# Transform the aggregated values back to the original DataFrame
df['TotalSubTotalByStatus'] = df.groupby('Status')['SubTotal'].transform('sum')
df['TotalTaxAmtByStatus'] = df.groupby('Status')['TaxAmt'].transform('sum')
df['TotalFreightByStatus'] = df.groupby('Status')['Freight'].transform('sum')

# Display the first few rows of the updated dataframe
display(df)