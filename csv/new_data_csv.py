import csv
# Agregar nuevo producto
new_product = {
    'name': 'New Product',
    'price': 9.99,
    'quantity': 10,
    'brand': 'New Brand',
    'category': 'Accessories',
    'entry_date': '2022-01-01'
}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n') #Salto de linea
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)