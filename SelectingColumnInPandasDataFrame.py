# Select rows based on a condition

import pandas as pd

data = pd.read_csv("C://Users//200741//Desktop//Sample.csv", sep='[;]',engine='python', header = None)
sampleDataFrame = pd.DataFrame(data)

newDataFrame = sampleDataFrame[sampleDataFrame[3]=='S']
print(newDataFrame)

