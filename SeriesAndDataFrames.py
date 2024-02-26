import pandas as pd

# Series
# Series are a 1-d array (series has indexes and values) like a column in a spreadsheet.

list = []
for i in range(100, -100, -10):
    list.append(i)

sampleArray = pd.Series(list)

print(sampleArray)

# Pandas Series is like a column of the spreadsheet
# DataFrames are like the spreadsheet itself.

# Read Csv into DataFrames

data = pd.read_csv("C://Users//200741//Desktop//Sample.csv", sep='[;]',engine='python', header = None)
sampleDataFrame = pd.DataFrame(data)

print(sampleDataFrame)

print(sampleDataFrame[0])

