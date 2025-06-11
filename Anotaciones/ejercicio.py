# Implementa una funcion que procese una lista de diccionarios con informacion de 
# empleados, utilizando anotaciones de tipo

# 1. Recibiras una lista de diccionarios. Cada diccionario tendrá las claves: 
# "nombre, "edad" y "sueldo".

# 2. Debe devolver una lista de empleados que ganen mas de cierto sueldo
def employe_filter(employee_list: list, salary: float) -> list:
    return [emp['nombre'] for emp in employee_list if emp['sueldo'] > salary]

lista = [
    {"nombre": "Maria La del Barrio",
     "edad": 30,
     "sueldo": 30000
     },
    {"nombre": "Luis Miguel",
     "edad": 25,
     "sueldo": 25000
     },
    {"nombre": "Ana Bolena",
     "edad": 20,
     "sueldo": 20000
     },
     {"nombre": "Pepe Grillo",
     "edad": 20,
     "sueldo": 50000
     }
]

print(employe_filter(lista, 25000))


