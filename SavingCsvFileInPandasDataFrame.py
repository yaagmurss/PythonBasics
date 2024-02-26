# You can save Pandas dataframes as CSV files to using the method to_csv().

import pandas as pd

data = pd.read_csv("C://Users//200741//Desktop//Sample.csv", sep='[;]',engine='python', header = None)
sampleDataFrame = pd.DataFrame(data)

newDataFrame = sampleDataFrame[sampleDataFrame[3]=='S']

print(newDataFrame)

newDataFrame.to_csv('C://Users//200741//Desktop//Result.csv', sep=';', header = None)