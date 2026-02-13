import pandas as pd

df = pd.read_csv("data/processed/materials_feature_engineered.csv")

print("Summary Statistics:\n")
print(df.describe())

print("\nData Types:\n")
print(df.dtypes)

print("\nCheck for Missing Values:\n")
print(df.isnull().sum())
