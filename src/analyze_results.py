import pandas as pd

df = pd.read_csv("data/processed/materials_with_indices.csv")

print("\nTop 10 Most Sustainable Materials:")
print(df.sort_values("material_suitability_score", ascending=False)[
    ["material_name",
     "material_type",
     "material_suitability_score"]
].head(10))

print("\nTop 5 Lowest CO2 Materials:")
print(df.sort_values("co2_emission_score")[[
    "material_name",
    "co2_emission_score"
]].head(5))

print("\nTop 5 Cost Efficient Materials:")
print(df.sort_values("cost_efficiency_index", ascending=False)[[
    "material_name",
    "cost_efficiency_index"
]].head(5))

