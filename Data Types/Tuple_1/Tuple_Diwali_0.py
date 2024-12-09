products = [
    ('SKU001', 'Laptop', 'Electronics', 60000.0, 5),
    ('SKU002', 'Headphones', 'Electronics', 2000.0, 10),
    ('SKU003', 'Coffee Maker', 'Appliances', 3000.0, 7),
    ('SKU004', 'Blender', 'Appliances', 1500.0, 15),
    ('SKU005', 'Notebook', 'Stationery', 50.0, 100),
    ('SKU006', 'Pen', 'Stationery', 10.0, 500)
]

category_totals = []

for product in products:
    sku, name, category, price, quantity = product
    total_value = price * quantity

    found = False
    for i in range(len(category_totals)):
        if category_totals[i][0] == category:
            category_totals[i] = (category, category_totals[i][1] + total_value)
            found = True
            break

    if not found:
        category_totals.append((category, total_value))

print("Total inventory value per category: ")
for category, total in category_totals:
    print(f"{category}: ₹{total:.2f}")
