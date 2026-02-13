import pandas as pd

# Load raw material dataset
df = pd.read_csv("data/raw/materials_raw.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill numerical missing values with median (industry standard practice)
numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns

for col in numerical_cols:
    df[col].fillna(df[col].median(), inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df.to_csv("data/processed/materials_cleaned.csv", index=False)

print("\nData cleaning complete.")
