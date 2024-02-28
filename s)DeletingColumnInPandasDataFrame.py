import pandas as pd

data = pd.read_csv("*//Sample.csv", sep='[;]', engine='python', header=None)
sampleDataFrame = pd.DataFrame(data)

print(sampleDataFrame)


# Del method changes the original data frame.

del sampleDataFrame[11]
print(sampleDataFrame)

print("---")
# drop() does not do the changes in the data frame itself

newSampleDataFrame = sampleDataFrame.drop(10, axis=1)

print("---")
# In order to do the changes in the original data frame itself, you can pass another argument inplace = True.
# You can also delete multiple columns at the same time bypassing the list of columns.

sampleDataFrame.drop([1, 2, 3], inplace=True, axis=1)
print(sampleDataFrame)


#newSampleDataFrame = sampleDataFrame.drop(10, axis=0)

#print(newSampleDataFrame)
