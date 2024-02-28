import pandas as pd
# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
					'Name': ['ABC', 'PQR', 'DEF', 'GHI']})

# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
					'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})

#Join Data In Pandas Data Frames

frames = [df1, df2]

result = pd.concat(frames)
display(result)
