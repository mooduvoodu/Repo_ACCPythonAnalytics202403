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

display(sales)
display(customers)

#Cross
# Adding a temporary key for cross join
sales['tmp'] = 1
customers['tmp'] = 1

# Performing cross join
cross_join = pd.merge(sales, customers, on='tmp').drop('tmp', axis=1)

# Displaying the result
display(cross_join)


# Performing inner join
inner_join = pd.merge(sales, customers, on='customer_id', how='inner')

display(inner_join)


# Performing left outer join
left_outer_join = pd.merge(sales, customers, on='customer_id', how='outer')

# Displaying the result
display(left_outer_join)