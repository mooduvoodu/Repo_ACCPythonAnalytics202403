
# First, let's read the uploaded CSV file and fix corrupt CR LF that is meessing up some rows
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

# Step 1: Convert TIMESTAMP_TOUCHPOINT to datetime
df['TIMESTAMP_TOUCHPOINT'] = pd.to_datetime(df['TIMESTAMP_TOUCHPOINT'], dayfirst=True)

# Step 2: For each customer with revenue, identify the timestamp of their purchase
purchase_timestamps = df[df['REVENUE'].notna()].groupby('CUSTOMERID')['TIMESTAMP_TOUCHPOINT'].max().reset_index(name='PURCHASE_TIMESTAMP')

# Merge the purchase timestamps back into the original dataframe
df = df.merge(purchase_timestamps, on='CUSTOMERID', how='left')

# Step 3: Filter to only include touchpoints up to and including the purchase timestamp
filtered_df = df[df['TIMESTAMP_TOUCHPOINT'] <= df['PURCHASE_TIMESTAMP']]

# Now, perform the same analysis as before, attributing revenue based on filtered touchpoints
# Count the number of touchpoints for each customer who made a purchase, using the filtered dataframe
filtered_customer_touchpoints = filtered_df.groupby('CUSTOMERID')['MARKETINGCHANNEL'].nunique().reset_index(name='TOUCHPOINTS')

# Merge this count back into the revenue_customers dataframe
revenue_customers = df[df['REVENUE'].notna()].drop_duplicates(subset=['CUSTOMERID']).merge(filtered_customer_touchpoints, on='CUSTOMERID')

# Calculate attributed revenue by dividing the total revenue by the number of touchpoints for each customer
revenue_customers['ATTRIBUTED_REVENUE'] = revenue_customers['REVENUE'] / revenue_customers['TOUCHPOINTS']

# Distribute this attributed revenue back to all interactions in the filtered dataframe
filtered_df = filtered_df.merge(revenue_customers[['CUSTOMERID', 'ATTRIBUTED_REVENUE']], on='CUSTOMERID', how='left')

# Sum attributed revenue by marketing channel in the filtered dataset
filtered_revenue_by_channel = filtered_df.groupby('MARKETINGCHANNEL')['ATTRIBUTED_REVENUE'].sum().reset_index()

filtered_revenue_by_channel.sort_values(by='ATTRIBUTED_REVENUE', ascending=False)


# Merge the attributed revenue information with the filtered dataset
filtered_df = filtered_df.drop(columns=['ATTRIBUTED_REVENUE'], errors='ignore') # Remove the column if it exists to prevent conflicts
filtered_df = filtered_df.merge(revenue_customers[['CUSTOMERID', 'ATTRIBUTED_REVENUE']], on='CUSTOMERID', how='left')

# Ensure the merge includes only those interactions before or at the purchase time, which it does now
# Now, sum the attributed revenue by marketing channel again
filtered_revenue_by_channel_corrected = filtered_df.groupby('MARKETINGCHANNEL')['ATTRIBUTED_REVENUE'].sum().reset_index()

filtered_revenue_by_channel_corrected.sort_values(by='ATTRIBUTED_REVENUE', ascending=False)

display(filtered_revenue_by_channel_corrected)


