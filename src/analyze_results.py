import pandas as pd

df = pd.read_csv("data/processed/materials_with_indices.csv")

categories = df["product_category"].unique()

for category in categories:
    print(f"\nTop 3 Materials for {category}:")
    subset = df[df["product_category"] == category]
    print(subset.sort_values(
        "material_suitability_score",
        ascending=False
    )[[
        "material_name",
        "material_type",
        "material_suitability_score"
    ]].head(3))
