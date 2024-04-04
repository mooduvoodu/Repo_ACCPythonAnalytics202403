# First, let's read the uploaded CSV file to understand its structure and contents.
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/classfiles/customerattributiondata - Sheet1 (1).csv')

# Display the first few rows of the DataFrame to understand its structure
print(df.head())

# Check for the presence of revenue data
revenue_data_present = df['REVENUE'].notna().sum()

# Get a summary of revenue data to understand its distribution
revenue_summary = df[df['REVENUE'].notna()]['REVENUE'].describe()

# Count the number of unique customers and marketing channels
unique_customers = df['CUSTOMERID'].nunique()
unique_marketing_channels = df['MARKETINGCHANNEL'].nunique()

print(revenue_data_present, revenue_summary, unique_customers, unique_marketing_channels)

# Filter rows with revenue and drop duplicates to ensure each customer is counted once
revenue_customers = df[df['REVENUE'].notna()].drop_duplicates(subset=['CUSTOMERID'])

# For each customer with revenue, count the number of touchpoints (unique marketing channels) they had
customer_touchpoints = df[df['CUSTOMERID'].isin(revenue_customers['CUSTOMERID'])].groupby('CUSTOMERID')['MARKETINGCHANNEL'].nunique().reset_index(name='TOUCHPOINTS')

# Merge this count back to the revenue_customers dataframe
revenue_customers = revenue_customers.merge(customer_touchpoints, on='CUSTOMERID')

# Calculate attributed revenue by dividing the total revenue by the number of touchpoints for each customer
revenue_customers['ATTRIBUTED_REVENUE'] = revenue_customers['REVENUE'] / revenue_customers['TOUCHPOINTS']

# Now, distribute this attributed revenue back to all interactions (not just the ones that directly led to revenue)
df = df.merge(revenue_customers[['CUSTOMERID', 'ATTRIBUTED_REVENUE']], on='CUSTOMERID', how='left')

# Sum attributed revenue by marketing channel
revenue_by_channel = df.groupby('MARKETINGCHANNEL')['ATTRIBUTED_REVENUE'].sum().reset_index()

revenue_by_channel.sort_values(by='ATTRIBUTED_REVENUE', ascending=False)

display(revenue_by_channel)

