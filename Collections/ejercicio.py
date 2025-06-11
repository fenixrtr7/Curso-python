# Implementa un sistema de gestion de pedidos utilizando colecciones y 
# enumeraciones
# 1. usar defaultdict
# Enumeracion para estado de la orden y contador

from collections import defaultdict
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 # Pendiente
    SHIPPED = 2 # Enviado
    DELIVERED = 3 # Entregado
"""
def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet', 'tablet']"""

# Clase para representar un pedido
class Order:
    def __init__(self, id: int, status: OrderStatus = OrderStatus.PENDING) -> None:
        self.id = id
        self.status = status
    
    def get_status(self):
        # print(f"status: {self.status}")
        # print(f"status.name: {self.status.name}")
        # print(f"status.value: {self.status.value}")
        match self.status:
            case OrderStatus.PENDING:
                return "Pendiente de envío"
            case OrderStatus.SHIPPED:
                return "Enviado"
            case OrderStatus.DELIVERED:
                return "Entregado"
    
    """def __repr__(self) -> str:
        return f"Pedido #{self.id} [{self.get_status()}]"""