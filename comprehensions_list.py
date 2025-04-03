squares = [x**2 for x in range(1, 11)]
print("Cuadrados: ", squares)

celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print("Fahrenheit: ", fahrenheit)

#Numeros pares
pares = [x for x in range(1, 11) if x % 2 == 0]
print("Pares: ", pares) 

#Numeros impares
impares = [x for x in range(1, 11) if x % 2 != 0]
print("Impares: ", impares) 

matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Matriz: ", matrix)
print("Matriz transpuesta: ", transposed)

dobleNum = [x*2 for x in range (1, 6)]
print("El doble del numero: ", dobleNum)

#Filtrar y transformar
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra)>3]
print("Palabras filtradas y en mayúsculas:", palabras_filtradas)

claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]
diccionario = {claves[i] : valores[i] for i in range(len(claves))}
print("Diccionario creado:", diccionario)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
traspuesta = [[raw[i]for raw in matriz] for i in range(len(matriz[0]))]
print("Transpuesta: ", traspuesta)

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

personasMadrid = [persona["nombre"] for persona in personas if persona["edad"] > 30 and persona["ciudad"] == "Madrid"]
print("Nombres de personas en Madrid mayores de 30 años:", personasMadrid)

#Numeros pares
pares = [x for x in range(1, 11) if x % 2 == 0]
print("Pares: ", pares)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paresMultiplicados = [x * 2 if x % 2 == 0 else x for x in numeros]
print("Números transformados:", paresMultiplicados)

