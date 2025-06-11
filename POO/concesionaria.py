# Desarrolla una concesionaria de vehículos en la cual se puedan 
# gestionar las compras y ventas de vehículos. 

# Un usuario podrá ver los vehículos disponibles, su precio y 
# realizar la compra de uno. 

# Aplica los conceptos de programación orientada a objetos 
# vistos en este ejercicio.

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.is_available = True

    def check_availability(self):
        return self.is_available
    
    def get_price(self):
        return self.precio

class Concesionaria:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        self.vehiculos = []
        self.usuarios = []
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido agregado")
    
    def eliminar_vehiculo(self, vehiculo):
        self.vehiculos.remove(vehiculo)
        print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido eliminado")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"El usuario {usuario.nombre} ha sido agregado")
    
    def eliminar_usuario(self, usuario):
        self.usuarios.remove(usuario)
        print(f"El usuario {usuario.nombre} ha sido eliminado")

    def mostrar_vehiculos(self):
        print("Vehiculos disponibles:")
        for vehiculo in self.vehiculos:
            print(f"- {vehiculo.marca} {vehiculo.modelo} - ${vehiculo.precio}")
    
    def comprar_vehiculo(self, vehiculo, usuario):
        if vehiculo.precio > usuario.dinero:
            print("No tienes suficiente dinero para comprar este vehiculo")
        else:
            usuario.dinero -= vehiculo.precio    
            self.vehiculos.remove(vehiculo)
            print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido comprado")

    def vender_vehiculo(self, vehiculo, usuario):
        usuario.dinero += vehiculo.precio
        self.vehiculos.append(vehiculo)
        print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido vendido")

class Usuario:
    def __init__(self, nombre, id, dinero):
        self.nombre = nombre
        self.id = id
        self.vehiculos_disponibles = []
        self.dinero = dinero
    
    def Dinero_disponible(self):
        print(f"El dinero disponible ${self.dinero}")


Usuario1 = Usuario("Javier", 1, 1000)
Usuario2 = Usuario("Javier", 2, 1000)

Concesionaria1 = Concesionaria("Concesionaria 1")

Vehiculo1 = Vehiculo("Toyota", "Corolla", 1000)
Vehiculo2 = Vehiculo("Honda", "Civic", 2000)
Vehiculo3 = Vehiculo("Ford", "Mustang", 3000)

Concesionaria1.agregar_vehiculo(Vehiculo1)
Concesionaria1.agregar_vehiculo(Vehiculo2)
Concesionaria1.agregar_vehiculo(Vehiculo3)

Concesionaria1.mostrar_vehiculos()

Concesionaria1.comprar_vehiculo(Vehiculo1, Usuario1)
Usuario1.Dinero_disponible()
        