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

print(customers.head(3))
print(sales.head(3))

sales['key'] = 1
customers['key'] = 1
cross_join = pd.merge(sales, customers, on='key').drop('key', axis=1)
print(cross_join)

inner_join = pd.merge(sales, customers, on='customer_id', how='inner')
print(inner_join)


right_outer_join = pd.merge(sales, customers, on='customer_id', how='right')
print(right_outer_join)
print(right_outer_join[right_outer_join['sales_amount'].isnull()])

left_outer_join = pd.merge(sales, customers, on='customer_id', how='left')
print(left_outer_join)
print(left_outer_join[left_outer_join['customer_name'].isnull()])



full_outer_join = pd.merge(sales, customers, on='customer_id', how='outer')
print(full_outer_join)
print(full_outer_join[full_outer_join['sales_amount'].isnull() | full_outer_join['customer_name'].isnull()])


total_sales_per_customer = inner_join.groupby('customer_name')['sales_amount'].sum().reset_index()
print(total_sales_per_customer)


inner_join['tax'] = inner_join['sales_amount'] * 0.10
print(inner_join)