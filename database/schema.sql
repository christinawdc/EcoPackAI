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