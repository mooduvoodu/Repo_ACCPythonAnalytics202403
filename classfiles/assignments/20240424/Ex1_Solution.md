
### Solutions and Explanations

**Solution to Exercise 1:**
```python
print(sales.head(3))
print(customers.head(3))
```

**Solution to Exercise 2:**
```python
sales['key'] = 1
customers['key'] = 1
cross_join = pd.merge(sales, customers, on='key').drop('key', axis=1)
print(cross_join)
```

**Solution to Exercise 3:**
```python
inner_join = pd.merge(sales, customers, on='customer_id', how='inner')
print(inner_join)
```

**Solution to Exercise 4:**
```python
right_outer_join = pd.merge(sales, customers, on='customer_id', how='right')
print(right_outer_join)
print(right_outer_join[right_outer_join['sales_amount'].isnull()])
```

**Solution to Exercise 5:**
```python
left_outer_join = pd.merge(sales, customers, on='customer_id', how='left')
print(left_outer_join)
print(left_outer_join[left_outer_join['customer_name'].isnull()])
```

**Solution to Exercise 6:**
```python
full_outer_join = pd.merge(sales, customers, on='customer_id', how='outer')
print(full_outer_join)
print(full_outer_join[full_outer_join['sales_amount'].isnull() | full_outer_join['customer_name'].isnull()])
```

**Solution to Exercise 7:**
```python
total_sales_per_customer = inner_join.groupby('customer_name')['sales_amount'].sum().reset_index()
print(total_sales_per_customer)
```

**Solution to Exercise 8:**
```python
inner_join['tax'] = inner_join['sales_amount'] * 0.10
print(inner_join)
```

### Explanation of Solutions

These exercises provide hands-on practice with various types of joins to understand how they manipulate and combine data differently in pandas:
- **Cross Join** creates a Cartesian product, useful for combining every instance of one dataset with every instance of another.
- **Inner Join** finds common records, essential for correlating data across tables.
- **Right and Left Outer Joins** are used to identify missing data in either the primary or secondary table.
- **Full Outer Join** provides a complete picture of both datasets, highlighting all discrepancies.
- **Aggregation and Calculation Exercises** (7 and 8) showcase how to further manipulate and analyze data once it has been merged.
