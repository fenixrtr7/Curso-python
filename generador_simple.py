lista = [1, 2, 3, 4]

iterador = iter(lista)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

text = "hola mundo"

iterador_texto = iter(text)

for caracter in iterador_texto:
    print(caracter)

limite = 10
iterador_impares = iter(range(1, limite + 1, 2))

for numero in iterador_impares:
    print("impar: ", numero)

iterador_pares = iter(range(0, limite + 1, 2))

for numero in iterador_pares:
    print("par: ", numero)

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(10):
    print(num)