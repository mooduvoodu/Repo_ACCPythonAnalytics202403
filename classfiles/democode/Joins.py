import pandas as pd

# Example DataFrame 1
data1 = {'key': ['A', 'B', 'C', 'D'],
         'value1': [1, 2, 3, 4]}
df1 = pd.DataFrame(data1)

# Example DataFrame 2
data2 = {'key': ['B', 'D', 'E', 'F'],
         'value2': [5, 6, 7, 8]}
df2 = pd.DataFrame(data2)

# Creating a temporary key for cross join
df1['tmp'] = 1
df2['tmp'] = 1

# Performing cross join
cross_join = pd.merge(df1, df2, on='tmp').drop('tmp', axis=1)

# Displaying the result
print(cross_join)

# Performing inner join
inner_join = pd.merge(df1, df2, on='key', how='inner')

# Displaying the result
print(inner_join)

# Performing left outer join
left_outer_join = pd.merge(df1, df2, on='key', how='left')

# Displaying the result
print(left_outer_join)

# Performing right outer join
right_outer_join = pd.merge(df1, df2, on='key', how='right')

# Displaying the result
print(right_outer_join)

# Performing full outer join
full_outer_join = pd.merge(df1, df2, on='key', how='outer')

# Displaying the result
print(full_outer_join)