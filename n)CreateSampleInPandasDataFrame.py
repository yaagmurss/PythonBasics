
import pandas as pd

# Create a sample pandas DataFrame object
df = pd.DataFrame({'QueueItem': ['QueueItem1', 'QueueItem2', 'QueueItem3', 'QueueItem4', 'QueueItem5'],
                   'FilePath': ['TestPath1', 'TestPath2', 'TestPath3', 'TestPath4', 'TestPath5']})

# Print the created pandas DataFrame
print('Sample pandas DataFrame:\n')
print(df)

# Create a Python list object with all the column values
l_row = ["QueueItem6", "TestPath6"]

# Append the above Python list object as a row to the existing pandas DataFrame
# Using the DataFrame.loc[]
df.loc[7] = l_row

# Print the modified pandas DataFrame object after addition of a row
print('Modified Sample pandas DataFrame:\n')
print(df)
