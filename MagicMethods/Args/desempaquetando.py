def suma(a, b, c):
    return a + b + c

# Desempaquetado de lista
valores = [1, 2, 3]
print(suma(*valores))  # Retorna 6

def mostrar_informacion(name, age):
    print(f"Name: {name}, Age: {age}")

# Desempaquetado de diccionario
datos = {'name': 'Carlos', 'age': 30}
mostrar_informacion(**datos)
