import pandas as pd

df = pd.read_csv("data/raw/materials_raw.csv")

print("Strength Range:")
print(df["strength_score"].min(), "-", df["strength_score"].max())

print("\nCO2 Emission Range:")
print(df["co2_emission_score"].min(), "-", df["co2_emission_score"].max())

print("\nGrouped by Material Type:")
print(df.groupby("material_type")[["strength_score","co2_emission_score"]].mean())
