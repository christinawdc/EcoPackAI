import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/raw/materials_raw.csv")

# -------------------------------
# 1️⃣ NORMALIZATION FUNCTIONS
# -------------------------------

def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())


# -------------------------------
# 2️⃣ NORMALIZE RELEVANT COLUMNS
# -------------------------------

df["norm_co2"] = min_max_normalize(df["co2_emission_score"])
df["norm_cost"] = min_max_normalize(df["cost_per_unit"])
df["norm_strength"] = min_max_normalize(df["strength_score"])
df["norm_recyclability"] = min_max_normalize(df["recyclability_percent"])
df["norm_biodegradability"] = min_max_normalize(df["biodegradability_score"])


# -------------------------------
# 3️⃣ CO2 IMPACT INDEX
# Lower CO2 = Better
# -------------------------------

df["co2_impact_index"] = 1 - df["norm_co2"]


# -------------------------------
# 4️⃣ COST EFFICIENCY INDEX
# Lower cost + Higher strength
# -------------------------------

df["cost_efficiency_index"] = (
    0.6 * (1 - df["norm_cost"]) +
    0.4 * df["norm_strength"]
)


# -------------------------------
# 5️⃣ MATERIAL SUITABILITY SCORE
# Multi-factor weighted index
# -------------------------------

df["material_suitability_score"] = (
    0.30 * df["co2_impact_index"] +
    0.25 * df["cost_efficiency_index"] +
    0.20 * df["norm_recyclability"] +
    0.15 * df["norm_biodegradability"] +
    0.10 * df["norm_strength"]
)

# -------------------------------
# Save Processed File
# -------------------------------

df.to_csv("data/processed/materials_with_indices.csv", index=False)

print("Index calculation complete.")
