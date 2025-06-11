import statistics
import csv

# Leer los datos de venta mensuales desde un archivo CSV
monthly_sales = {}
with open('Ventas/monthly_sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
#print(sales)

mean = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)

print(f"Media: {mean}")
print(f"Mediana: {median}")
print(f"Moda: {mode}")

# Desviacion estandar
std_dev = statistics.stdev(sales)
print(f"Desviación estandar: {std_dev}")

# Varianza
variance = statistics.variance(sales)
print(f"Varianza: {variance}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f"Rango de ventas: {range_sales}")