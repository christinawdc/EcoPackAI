import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/materials_raw.csv")

np.random.seed(42)

def adjust_strength(row):
    if row["material_type"] == "Fiber":
        return np.random.uniform(4,7)
    elif row["material_type"] == "Bioplastic":
        return np.random.uniform(5,7)
    elif row["material_type"] == "Plastic":
        return np.random.uniform(6,8)
    elif row["material_type"] == "Glass":
        return np.random.uniform(7,9)
    elif row["material_type"] == "Metal":
        return np.random.uniform(8,10)
    else:
        return row["strength_score"]

def adjust_co2(row):
    name = row["material_name"]

    if "Cardboard" in name or "Paper" in name or "Pulp" in name:
        return np.random.uniform(0.6,1.3)
    elif "PLA" in name or "PHA" in name:
        return np.random.uniform(1.0,2.5)
    elif "PET" in name:
        return np.random.uniform(2.0,3.5)
    elif "Glass" in name:
        return np.random.uniform(1.0,1.8)
    elif "Aluminum" in name:
        return np.random.uniform(8,12)
    elif "Steel" in name:
        return np.random.uniform(1.8,2.5)
    else:
        return row["co2_emission_score"]

df["strength_score"] = df.apply(adjust_strength, axis=1)
df["co2_emission_score"] = df.apply(adjust_co2, axis=1)

df.to_csv("data/raw/materials_raw.csv", index=False)

print("Industry alignment complete.")
