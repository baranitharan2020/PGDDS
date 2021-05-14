import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv'
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv')
df.set_index(['Office','Department'],inplace=True)
# Provide your answer below
df.sort_index(inplace=True)
print(df.head())
