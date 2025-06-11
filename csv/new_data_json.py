import json

file_path = 'products.json'

new_product = {
    'name': 'New Product',
    'price': 9.99,
    'quantity': 10,
    'brand': 'New Brand',
    'category': 'Accessories',
    'entry_date': '2022-01-01'
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)