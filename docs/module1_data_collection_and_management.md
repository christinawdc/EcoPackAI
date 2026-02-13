# Module 1: Data Collection and Management

1. Overview

Module 1 focuses on structured data acquisition, validation, and storage for the AI Framework for Sustainable Packaging Design and Material Optimization system.

The objective of this module was to:

- Collect eco-friendly material data aligned with industry standards

- Collect industry product category data

- Validate numerical ranges using lifecycle assessment (LCA) logic

- Design and implement a PostgreSQL database schema

- Integrate CSV datasets into the database with schema validation

This module establishes the foundational data layer for subsequent optimization and recommendation models.

2. Materials Dataset
   2.1 Dataset Description

A structured materials dataset was created containing sustainability, performance, and cost-related attributes.

## Attributes Included

| Attribute                | Description                                         |
| ------------------------ | --------------------------------------------------- |
| material_id              | Unique identifier                                   |
| material_name            | Name of packaging material                          |
| material_type            | Fiber / Plastic / Metal / Bioplastic / Glass        |
| product_category         | Applicable industry category                        |
| strength_score           | Structural strength rating (industry-aligned range) |
| weight_capacity_kg       | Load-bearing capacity                               |
| biodegradability_score   | Environmental degradation rating                    |
| co2_emission_score       | CO₂ emission per kg (aligned with LCA standards)    |
| recyclability_percent    | Percentage recyclability                            |
| cost_per_unit            | Economic cost metric                                |
| recycled_content_percent | Circular economy metric                             |

2.2 Industry Standard Alignment

Strength and CO₂ values were adjusted to reflect approximate lifecycle assessment ranges:

Example CO₂ Ranges (kg CO₂/kg material)

Corrugated cardboard: ~0.6 – 1.3

PLA / Bioplastics: ~1.0 – 2.5

PET plastics: ~2.0 – 3.5

Glass: ~1.0 – 1.8

Steel: ~1.8 – 2.5

Aluminum: ~8 – 12

Strength ranges were differentiated by material type to reflect structural realism.

Validation scripts were implemented to verify:

- Minimum and maximum ranges

- Category-level mean values

- Logical differentiation across material types

3. Product Dataset
   3.1 Dataset Description

A structured product dataset was created across major industry sectors:

- Electronics

- Food

- Cosmetics

- Pharmaceuticals

- E-commerce

A total of 1000 products were generated (200 per category).

## Attributes Included

| Attribute               | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| product_id              | Unique identifier                                      |
| product_name            | Real-world product type (e.g., Laptop, Perfume Bottle) |
| product_category        | Industry category                                      |
| weight_kg               | Product weight                                         |
| fragility_score         | Fragility rating (1–10)                                |
| strength_requirement    | Required packaging strength                            |
| sustainability_priority | Sustainability importance (1–10)                       |
| cost_sensitivity        | Cost sensitivity (1–10)                                |

Strength requirements were partially correlated with fragility to simulate realistic packaging constraints.

4. Data Processing & Index Computation

The following sustainability indices were computed:

4.1 CO₂ Impact Index

Normalized inverse of CO₂ emissions:

Lower emissions → Higher index value

4.2 Cost Efficiency Index

Weighted combination of:

Inverse normalized cost

Normalized strength

4.3 Material Suitability Score

Multi-factor weighted score combining:

CO₂ impact

Cost efficiency

Recyclability

Biodegradability

Strength

All values were normalized using Min-Max scaling prior to index calculation.

Processed dataset was stored as:

materials_with_indices.csv

5. PostgreSQL Database Design
   5.1 Database Created

Database name:

ecopackai

5.2 Materials Table Schema
CREATE TABLE materials (
material_id INT PRIMARY KEY,
material_name VARCHAR(100),
material_type VARCHAR(50),
product_category VARCHAR(50),
strength_score FLOAT,
weight_capacity_kg FLOAT,
biodegradability_score FLOAT,
co2_emission_score FLOAT,
recyclability_percent FLOAT,
cost_per_unit FLOAT,
recycled_content_percent FLOAT,
co2_impact_index FLOAT,
cost_efficiency_index FLOAT,
material_suitability_score FLOAT
);

5.3 Products Table Schema
CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
product_category VARCHAR(50),
weight_kg FLOAT,
fragility_score INT,
strength_requirement FLOAT,
sustainability_priority INT,
cost_sensitivity INT
);

6. Data Integration

CSV files were imported into PostgreSQL using pgAdmin:

materials_with_indices.csv → materials table

products_raw.csv → products table

Validation steps included:

Row count verification

Schema validation using information_schema.columns

Data type verification

Primary key constraint validation

7. Outcome of Module 1

By completion of Module 1, the system includes:

Industry-aligned material dataset

Realistic product dataset

Validated sustainability metrics

Multi-criteria scoring framework

Structured PostgreSQL relational database

Reproducible ingestion pipeline

This establishes a clean and scalable data foundation for:

Material-to-product optimization

Recommendation systems

Sustainability analytics

Machine learning integration (future modules)

Module 1 Status: Complete

The data layer is fully structured, validated, and database-integrated, enabling progression to Module 2
