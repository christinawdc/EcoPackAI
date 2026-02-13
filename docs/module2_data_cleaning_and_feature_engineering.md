Module 2: Data Cleaning and Feature Engineering

1. Overview

Module 2 focuses on preparing the material dataset for analytical modeling and optimization. This phase ensures that the dataset is:

Clean
Normalized
Numerically consistent
Machine learning ready
Statistically validated

## This module transforms raw structured data into a processed feature-engineered dataset suitable for sustainability scoring and future optimization algorithms.

2. Data Cleaning
   2.1 Missing Value Handling

Although the dataset was synthetically generated, industry-standard data cleaning procedures were implemented to ensure robustness.

Approach Used:

Identified missing values using isnull().sum()
Numerical columns were imputed using median substitution
Median imputation was selected because:
It is robust to outliers
It preserves distribution better than mean imputation

It is widely used in industry data preprocessing pipelines

Output File:

```
materials_cleaned.csv
```

---

3. Feature Normalization

To ensure consistent scale across numerical attributes, Min-Max normalization was applied.

Formula Used:
Xnormalised= (X-Xmin)/(Xmax-Xmin)

Normalized Features:

- CO₂ emission score
- Cost per unit
- Strength score
- Recyclability percentage
- Biodegradability score

Normalization ensures:

- Fair weighting across indices
- Prevention of dominance by large-scale variables
- Compatibility with machine learning models

4. Feature Engineering

Three composite sustainability indices were engineered.

4.1 CO₂ Impact Index

Lower emissions are preferred.
CO2 Impact Index=1−normalized CO2

Interpretation:
Higher value → Lower environmental impact

4.2 Cost Efficiency Index

Balances cost and structural strength.
Cost Efficiency Index=0.6(1−normalized cost)+0.4(normalized strength)

Interpretation:
Favors lower cost materials
Rewards stronger materials

4.3 Material Suitability Score

A weighted multi-criteria sustainability score:
Material Suitability Score=0.30(CO2 Impact Index)+0.25(Cost Efficiency Index)+0.20(Recyclability)++0.15(Biodegradability)+0.10(Strength)

This score integrates:

Environmental impact
Economic feasibility
Circular economy metrics
Structural reliability

The weighting structure reflects sustainability-driven decision modeling.

5. Categorical Encoding

Categorical attributes:

material_type
product_category
Were encoded using One-Hot Encoding.
Method:
pd.get_dummies(..., drop_first=True)

Purpose:
Convert categorical variables into numeric format
Avoid multicollinearity
Enable compatibility with ML models
This prepares the dataset for predictive modeling and similarity-based recommendation systems.

6. Data Validation

To ensure integrity, the following validation steps were executed:
Summary statistics using df.describe()
Data type verification
Missing value recheck
Range validation of engineered indices
Validation confirms:
No missing values
Proper normalization (values between 0 and 1)
Logical distribution of composite indices

7. Final Output
   Processed dataset:
   materials_feature_engineered.csv
   This dataset contains:

Cleaned data

Normalized numerical features
Encoded categorical features
Computed sustainability indices

It is now:
✔ Database-ready
✔ ML-ready
✔ Optimization-ready

Module 2 Status: Complete

The dataset has been fully cleaned, transformed, and engineered into a structured analytical format. It is prepared for:
Material-to-product optimization
Recommendation system development
Machine learning modeling
Advanced sustainability analytics
