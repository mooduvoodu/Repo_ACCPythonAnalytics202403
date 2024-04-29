import pandas as pd

# Example sales DataFrame
data_sales = {
    'customer_id': [1, 2, 1, 3],
    'sales_amount': [100, 200, 150, 400]
}
sales = pd.DataFrame(data_sales)

# Example customers DataFrame
data_customers = {
    'customer_id': [1, 2, 4],
    'customer_name': ['Alice', 'Bob', 'Charlie']
}
customers = pd.DataFrame(data_customers)

def calculate_discount(row):
    return row['sales_amount'] * 0.15

sales['discount_amount'] = sales.apply(calculate_discount, axis=1)
print(sales)

def tag_customer(row):
    return "Priority" if row['customer_name'].startswith('A') else "Standard"

customers['customer_status'] = customers.apply(tag_customer, axis=1)
print(customers)

concatenated_df = pd.concat([sales, customers], axis=0)
print(concatenated_df)

combined_sales = pd.concat([sales, sales], axis=1)
print(combined_sales)

def count_data_types(row):
    return 'Sales Data' if pd.notna(row['sales_amount']) else 'Customer Data'

concatenated_df['data_type'] = concatenated_df.apply(count_data_types, axis=1)
data_summary = concatenated_df['data_type'].value_counts()
print(data_summary)
