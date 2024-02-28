import pandas as pd

data = pd.read_csv("*//Sample.csv", sep='[;]',engine='python', header = None)
sampleDataFrame = pd.DataFrame(data)

print(sampleDataFrame)

#Adding Column

newColumn = [0,1,2,3,4,5,6,7,8,9,10]

sampleDataFrame['12'] =newColumn

print(sampleDataFrame)

newColumn = [0,1,2,3,4,5,6,7,8,9,10]

sampleDataFrame['13'] =newColumn

print(sampleDataFrame)

