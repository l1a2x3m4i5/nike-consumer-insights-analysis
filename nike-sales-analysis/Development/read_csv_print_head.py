import pandas as pd

df = pd.read_csv("NKE.csv", sep=",", skipinitialspace=True)

print(df.head())
print(df.columns)