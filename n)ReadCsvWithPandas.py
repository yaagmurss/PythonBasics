# Read csv

import pandas as pd

df = pd.read_csv('data.csv')

print(df) 

---
# maxRows

import pandas as pd

print(pd.options.display.max_rows) 

--

# sample = "totalbill_tip, sex:smoker, day_time, size
# 16.99, 1.01:Female|No, Sun, Dinner, 2
# 10.34, 1.66, Male, No|Sun:Dinner, 3
# 21.01:3.5_Male, No:Sun, Dinner, 3
#23.68, 3.31, Male|No, Sun_Dinner, 2
# 24.59:3.61, Female_No, Sun, Dinner, 4
# 25.29, 4.71|Male, No:Sun, Dinner, 4"

# Importing pandas library
import pandas as pd

# Load the data of csv
df = pd.read_csv('sample.csv',
				sep='[:, |_]',
				engine='python')

"""pd.read_csv(str(row["FilePath"]), sep='[;]',engine='python')"""

# Print the Dataframe
print(df)


------



