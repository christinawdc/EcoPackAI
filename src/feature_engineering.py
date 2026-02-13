import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/materials_cleaned.csv")

def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())

# Normalize numerical columns
df["norm_co2"] = min_max_normalize(df["co2_emission_score"])
df["norm_cost"] = min_max_normalize(df["cost_per_unit"])
df["norm_strength"] = min_max_normalize(df["strength_score"])
df["norm_recyclability"] = min_max_normalize(df["recyclability_percent"])
df["norm_biodegradability"] = min_max_normalize(df["biodegradability_score"])

# CO2 Impact Index
df["co2_impact_index"] = 1 - df["norm_co2"]

# Cost Efficiency Index
df["cost_efficiency_index"] = (
    0.6 * (1 - df["norm_cost"]) +
    0.4 * df["norm_strength"]
)

# Material Suitability Score
df["material_suitability_score"] = (
    0.30 * df["co2_impact_index"] +
    0.25 * df["cost_efficiency_index"] +
    0.20 * df["norm_recyclability"] +
    0.15 * df["norm_biodegradability"] +
    0.10 * df["norm_strength"]
)

df = pd.get_dummies(
    df,
    columns=["material_type", "product_category"],
    drop_first=True
)

df.to_csv("data/processed/materials_feature_engineered.csv", index=False)

print("Feature engineering complete.")

