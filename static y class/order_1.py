# 1 Un metodo estatico para verificar si el monto de un pedido 
# es mayor a un minimo permitido (ejemplo 50)

# 2 Un metodo de clase que permita crear un pedido aplicando un descuento global
class Order:
    global_discount = 10
    minimum_order_amount = 50

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount

    @classmethod
    def update_min_order_amount(cls, new_minimum):
        """Actuaiza el monto minimo de orden"""
        cls.minimum_order_amount = new_minimum

    @classmethod
    def _apply_discount(cls, amount):
        """Aplica el descuento global al monto"""
        return amount - (amount * (cls.global_discount / 100))

    @staticmethod 
    def validate_order(amount):
        """Valida si el monto cumple con el minimo requerido"""
        return amount >= Order.minimum_order_amount

    @classmethod
    def create_order(cls, amount):
        """Crea una orden si el monto es valido"""
        if cls.validate_order(amount):
            order_with_disccount = cls._apply_discount(amount)
            print(f"Order sended. Total to pay => ${order_with_disccount}")
            return order_with_disccount
        else:
            print(f"Order not valid")
            return None

print(Order.global_discount) # 10      
Order.update_global_discount(50)
print(Order.global_discount) # 50
print(Order.validate_order(20)) # False
print(Order.validate_order(90)) # True
Order.update_min_order_amount(100)
print(Order.minimum_order_amount)
print(Order.validate_order(20))
print(Order.validate_order(90)) 
Order.create_order(120) # Order sended. Total to pay => $60.0
Order.create_order(10) # Order not valid