import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

electronics_products = [
    "Laptop", "Tablet", "Smartphone", "Smartwatch",
    "Bluetooth Speaker", "Gaming Console",
    "Wireless Earbuds", "External Hard Drive",
    "Router", "Power Bank"
]

food_products = [
    "Chocolate Box", "Frozen Pizza", "Organic Honey Jar",
    "Cereal Box", "Protein Bar Pack",
    "Milk Carton", "Olive Oil Bottle",
    "Snack Chips Pack", "Tea Box", "Coffee Jar"
]

cosmetics_products = [
    "Perfume Bottle", "Lipstick Case",
    "Face Cream Jar", "Shampoo Bottle",
    "Makeup Palette", "Body Lotion",
    "Sunscreen Tube", "Serum Bottle",
    "Foundation Bottle", "Nail Polish"
]

pharma_products = [
    "Tablet Blister Pack", "Syrup Bottle",
    "Insulin Kit", "Vitamin Bottle",
    "First Aid Kit", "Injection Vial",
    "Capsule Container", "Medical Device Kit",
    "Thermometer", "Blood Pressure Monitor"
]

ecommerce_products = [
    "Clothing Package", "Book Shipment",
    "Shoe Box", "Home Decor Item",
    "Kitchen Appliance", "Fitness Equipment",
    "Toy Set", "Stationery Bundle",
    "Office Supplies Pack", "Gift Hamper"
]

category_map = {
    "Electronics": electronics_products,
    "Food": food_products,
    "Cosmetics": cosmetics_products,
    "Pharmaceuticals": pharma_products,
    "E-commerce": ecommerce_products
}

rows = []
product_id = 1

for category, product_list in category_map.items():
    for _ in range(200):  # 5 categories × 200 = 1000 products
        
        product_name = random.choice(product_list)

        weight = np.random.uniform(0.1, 15)
        fragility = np.random.randint(1, 11)

        # Strength requirement influenced by fragility
        strength_req = np.clip(fragility + np.random.uniform(-1, 2), 4, 10)

        sustainability_priority = np.random.randint(1, 11)
        cost_sensitivity = np.random.randint(1, 11)

        rows.append([
            product_id,
            product_name,
            category,
            round(weight, 2),
            fragility,
            round(strength_req, 2),
            sustainability_priority,
            cost_sensitivity
        ])

        product_id += 1

columns = [
    "product_id",
    "product_name",
    "product_category",
    "weight_kg",
    "fragility_score",
    "strength_requirement",
    "sustainability_priority",
    "cost_sensitivity"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("data/raw/products_raw.csv", index=False)

print("Product dataset created.")
