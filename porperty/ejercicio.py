# Implementa validacion para asegurarse de que el precio y
#  el stock no puedan ser negativos

# Define un metodo para eliminar la informacion del inventario

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._price = price
        self._stock = stock

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @price.deleter
    def price(self):
        print(f"The price of {self.name} has been deleted")
        del self._price
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = new_stock

    @stock.deleter
    def stock(self):
        print(f"The stock of {self.name} has been deleted")
        del self._stock

# Crear instancia de Producto
p1 = Product("Tijera", 50, 10)
print(p1.price) 
print(p1.stock) 

# Modificar el precio de forma controlada
p1.price = 6000
print(p1.price)  

# Intentar establecer un salario negativo
#p1.price = -1000  

# Eliminar el salario
del p1.price  
