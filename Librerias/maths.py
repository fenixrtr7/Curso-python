import math

#Hallar el area y preimetro de un circulo

radio = float(input("Ingrese el radio del circulo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")