import pandas as pd

data = pd.read_csv("C://Users//200741//Desktop//Sample.csv", sep='[;]', engine='python', header=None)
sampleDataFrame = pd.DataFrame(data)

print(sampleDataFrame)

sampleDataFrame.loc[sampleDataFrame.__len__()+1] = ['FON',
                                                    '26.02.2024',
                                                    '1',
                                                    'A',
                                                    'IOO',
                                                    '1',
                                                    'IPG',
                                                    '23906644',
                                                    '37344257.81',
                                                    '26.02.2024',
                                                    '26.02.2024',
                                                    'TL']




print(sampleDataFrame)
