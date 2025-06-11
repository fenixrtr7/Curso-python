# Crea una funcion que reciba una cantidad variable de productos y sus precios
# calcule el total y aplique un descuento opcional si se proporciona como un 
# argumento con nombre

# La clave está en discernir cuándo es necesario un 
# enfoque u otro y cómo podemos sacar provecho del 
# dinamismo que ofrecen estos mecanismos.

# 1. Usar args para recibir una lista de precios
# 2. Usar kwargs para aceptar un descuento opcional y 
# aplicarlo al total

class Venta:
    def __init__(self, *args, **kwargs):
        self.prices = args 
        self.discount = kwargs

    def calcular_total(self) -> float:
        print("Calculando totales")
        if self.discount:
            for key, value in self.discount.items():
                discount = value
                total = sum(self.prices)
                total_final = total - (discount / 100 * total)
            return print(f'El total fue: {total} se aplica descuento de {discount}, total final: {total_final}')
        else:
            print(f'El total fue: {sum(self.prices)}')

venta1 = Venta(200,300,500, discount=10)
venta2 = Venta(800,200)
venta3 = Venta(200,300,500,900, 1432, discount=20)
venta1.calcular_total()
venta2.calcular_total()
venta3.calcular_total()

        