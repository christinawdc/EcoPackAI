## Materials Table

| Column Name                | Data Type    | Description                                 | Unit / Range                                 |
| -------------------------- | ------------ | ------------------------------------------- | -------------------------------------------- |
| material_id                | INT          | Unique identifier for each material         | Positive integer                             |
| material_name              | VARCHAR(100) | Name of the packaging material              | Text                                         |
| material_type              | VARCHAR(50)  | Category of material                        | Fiber / Plastic / Metal / Bioplastic / Glass |
| cost_per_unit              | NUMERIC      | Cost per unit of material                   | USD / kg                                     |
| co2_emission_score         | NUMERIC      | Carbon footprint per kg                     | 0.6 – 12 (kg CO₂/kg)                         |
| strength_score             | NUMERIC      | Structural strength rating                  | 4 – 10                                       |
| recyclability_percentage   | NUMERIC      | Percentage of material that can be recycled | 0 – 100                                      |
| biodegradability_score     | NUMERIC      | Biodegradability rating                     | 0 – 10                                       |
| co2_impact_index           | NUMERIC      | Engineered index: lower CO₂ → higher score  | 0 – 1                                        |
| cost_efficiency_index      | NUMERIC      | Engineered index: balances cost & strength  | 0 – 1                                        |
| material_suitability_score | NUMERIC      | Weighted multi-factor sustainability score  | 0 – 1                                        |
| norm_co2                   | NUMERIC      | Normalized CO₂ emission score               | 0 – 1                                        |
| norm_cost                  | NUMERIC      | Normalized cost score                       | 0 – 1                                        |
| norm_strength              | NUMERIC      | Normalized strength score                   | 0 – 1                                        |
| norm_recyclability         | NUMERIC      | Normalized recyclability score              | 0 – 1                                        |
| norm_biodegradability      | NUMERIC      | Normalized biodegradability score           | 0 – 1                                        |

---
## Products Table
| Column Name                | Data Type    | Description                                 | Unit / Range                                 |
| -------------------------- | ------------ | ------------------------------------------- | -------------------------------------------- |
| product_id                 | INT          | Unique identifier for each product          | Positive integer                             |
| product_name               | VARCHAR(100) | Real-world product type                     | e.g., Laptop, Perfume Bottle                 |
| product_category           | VARCHAR(50)  | Industry category                           | Electronics,Food,Cosmetics,Pharma, E-commerce|
| weight_kg                  | NUMERIC      | Product weight                              | 0.1 – 15 kg                                  |
| fragility_score            | INT          | Fragility rating                            | 1 – 10                                       |
| strength_requirement       | NUMERIC      | Required packaging strength                 | 4 – 10                                       |
| sustainability_priority    | INT          | Importance of sustainability for product    | 1 – 10                                       |
| cost_sensitivity           | INT          | Cost sensitivity rating                     | 1 – 10                                       |
