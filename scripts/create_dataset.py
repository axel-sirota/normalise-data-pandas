import random

import numpy as np
import pandas as pd

number_of_rows = 5000
df_list = []
types_of_distributions = [lambda x: 4*np.random.sample() -5, lambda x: 10*np.random.sample() + 3, lambda x: 2*np.random.randn() + 5]

for index in range(number_of_rows):
    row = []
    for column_ix in range(3):
        func = types_of_distributions[column_ix]
        value = func(1)
        row.append(value)
    df_list.append(row)
df = pd.DataFrame(df_list, columns=["uniform_negative", "uniform_positive", "normal"])
df.to_csv('../data/data.csv', index=False)

