import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'A': [np.nan, 0.0, np.nan],
    'B': [3, 4, 5]
})

df2 = pd.DataFrame({
    'A': [1, 1, 3],
    'B': [3.0, np.nan, 3.0]
})

df3 = df1.combine_first(df2)

print(df3)