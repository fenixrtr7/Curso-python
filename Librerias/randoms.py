import random

#Generar un numero entero aleatorio
random_number = random.randint(1, 10)
print("Numero aleatorio: ", random_number)

#Elegir colores aleatoriamente
colors = ["rojo", "verde", "azul"]
random_color = random.choice(colors)
print("Color aleatorio: ", random_color)

#Barajar una lista de cartas
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print("Cartas barajadas: ", cards)