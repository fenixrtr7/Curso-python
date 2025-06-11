import csv

"""#Leer un CSV
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar la informacion por columnas 
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")