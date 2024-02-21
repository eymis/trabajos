import pandas as pd
import openpyxl

dataframe = pd.read_csv("data.csv")

print(dataframe)

print(dataframe["A"].mean())
print(dataframe["B"].max())
print(dataframe["B"].min())
print(dataframe["B"].median())
print(dataframe["C"].describe())