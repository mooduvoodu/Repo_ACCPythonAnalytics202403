#Using NFL penalty data set

# Concat - or Set operation in SQL (Union etc...)

import pandas as pd
import numpy

# Creating sample dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
df3 = pd.DataFrame({'C': [13, 14, 15], 'D': [16, 17, 18]})

df4 = pd.DataFrame({'A': [19, 20, 21], 'B': [22, 23, 24]}, index=[3, 4, 5])

# Concatenating dataframes vertically (axis=0)
vertical_concat = pd.concat([df1, df2])
display(vertical_concat)

# Concatenating dataframes horizontally (axis=1)
horizontal_concat = pd.concat([df1, df3], axis=1)
display(horizontal_concat)

# Concatenating with different index
different_index_concat = pd.concat([df1, df2], ignore_index=True)
display(different_index_concat)
# Concatenating with multi-level indexing (keys)
multi_index_concat = pd.concat([df1, df2], keys=['x', 'y'])
display(multi_index_concat)
# Displaying the results
print("Vertical Concatenation:")
print(vertical_concat)
print("\nHorizontal Concatenation:")
print(horizontal_concat)
print("\nConcatenation with Different Index:")
print(different_index_concat)
print("\nMulti-Level Index Concatenation:")
print(multi_index_concat)


#diff indexes

# Concatenating with different index (ignore_index=True)
different_index_concat = pd.concat([df1, df2], ignore_index=True)
display(different_index_concat)
# Concatenating with a non-overlapping index (df1 and df4)
non_overlapping_index_concat = pd.concat([df1, df4])
display(non_overlapping_index_concat)
# Concatenating with a partially overlapping index (ignore_index=True)
partially_overlapping_index_concat = pd.concat([df1, df4], ignore_index=True)

# Displaying the results
print("Concatenation with Different Index (Continuous Index):")
print(different_index_concat)
print("\nConcatenation with Non-Overlapping Index:")
print(non_overlapping_index_concat)
print("\nConcatenation with Partially Overlapping Index:")
print(partially_overlapping_index_concat)

# Diff column names


# Dataframes with different column names
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

# Vertical concatenation
vertical_concat = pd.concat([df1, df2], ignore_index=True)
display(vertical_concat)
print("Vertical Concatenation:")
print(vertical_concat)

# Horizontal concatenation
horizontal_concat = pd.concat([df1, df2], axis=1)

print("\nHorizontal Concatenation:")
print(horizontal_concat)

#inconsistent indexes

df2_different_index = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=[3, 4, 5])

# Horizontal concatenation with different indexes
horizontal_diff_index_concat = pd.concat([df1, df2_different_index], axis=1)
display(horizontal_diff_index_concat)
print("\nHorizontal Concatenation with Different Indexes:")
print(horizontal_diff_index_concat)

#Show common columns only - join=inner

# Creating sample dataframes with different column names
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'B': [7, 8, 9], 'C': [10, 11, 12]})

# Concatenating using 'inner' join to include only shared columns
inner_join_concat = pd.concat([df1, df2], join='inner', ignore_index=True)
#join will by default only include same index
print(inner_join_concat)


#Merge and Join
# a .join() method that uses .merge() under the hood. .join() will 
# merge dataframe objects based on an index, but the .merge() function is much more 
# explicit and flexible. If you are planning to merge dataframes by the row index,
#  for example, you might want to look into the .join() method.

log_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/NFLPenalties/log.csv')
players_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/NFLPenalties/players.csv')


# Setting 'Player' and 'Name' columns as indices for the respective dataframes
log_df_indexed = log_df.set_index('Player')
players_df_indexed = players_df.set_index('Name')


# The attempt to join the dataframes using the join() method resulted in a ValueError. 
# This error occurred because both dataframes contain columns with the same names, 
# such as 'Pos', 'Declined', 'Offsetting', 'Yards', 'Week', and 'Year'. The join()
#  method requires either unique column names across both dataframes or specified
#  suffixes to differentiate columns with the same name.
# To resolve this, we can specify suffixes that will be appended to the column names
#  of the left and right dataframes where there is a name clash. Let's modify the join() method call to include these suffixes and try again.

#common issue with join 
# Joining the dataframes on their indices
joined_df = log_df_indexed.join(players_df_indexed, how='inner')


# Joining the dataframes on their indices
joined_df = log_df_indexed.join(players_df_indexed, how='inner', lsuffix='_left', rsuffix='_right')

# Display the first few rows of the joined dataframe to check the result
joined_df_head = joined_df.head()

joined_df_head

 
# more join examples
# Pandas     SQL
# left       left outer
# right      right outer
# outer      full outer
# inner      inner


# Demonstrating different types of joins in pandas to mimic SQL joins



# Reload the data after execution state reset
log_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/NFLPenalties/log.csv')
players_df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics20231102/datasets/NFLPenalties/players.csv')


# Identifying the common column for joins
#  the 'Player' column in log_df could be matched with the 'Name' column in players_df
# Renaming the 'Name' column in players_df for consistency
players_df_renamed = players_df.rename(columns={"Name": "Player"})



# Performing different types of joins
# Left outer join
left_join_df = log_df.join(players_df_renamed.set_index('Player'), on='Player', how='left', lsuffix='_left', rsuffix='_right')

# Right outer join
right_join_df = log_df.join(players_df_renamed.set_index('Player'), on='Player', how='right', lsuffix='_left', rsuffix='_right')

# Full outer join
full_outer_join_df = log_df.join(players_df_renamed.set_index('Player'), on='Player', how='outer', lsuffix='_left', rsuffix='_right')

# Inner join
inner_join_df = log_df.join(players_df_renamed.set_index('Player'), on='Player', how='inner', lsuffix='_left', rsuffix='_right')

# Display the first few rows of each joined DataFrame to verify the joins
left_join_df.head(), right_join_df.head(), full_outer_join_df.head(), inner_join_df.head()


#Cross Join
#Not enough memory
# Creating a temporary key column in both DataFrames for cross join
log_df['key'] = 1
players_df_renamed['key'] = 1

# Performing the cross join
cross_join_df = log_df.join(players_df_renamed.set_index('key'), on='key', lsuffix='_log', rsuffix='_player')

# Dropping the temporary key column
cross_join_df.drop('key', axis=1, inplace=True)

# Display the first few rows of the cross joined DataFrame
cross_join_df.head()
