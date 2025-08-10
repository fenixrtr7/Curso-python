def new_order(order_id, customer_name, product_name, quantity):
    print(f"New order created: {order_id} for {customer_name}.")
    print(f"Product: {product_name}, Quantity: {quantity}")
    # Aquí podrías agregar lógica para procesar el pedido, como verificar stock, calcular total, etc.

def cancel_order(order_id):
    print(f"Order {order_id} has been canceled.")
    # Aquí podrías agregar lógica para cancelar el pedido, como actualizar el estado en la base de datos, etc.

def view_order(order_id):
    print(f"Viewing details for order {order_id}.")
    # Aquí podrías agregar lógica para recuperar y mostrar los detalles del pedido, como productos, cantidades, precios, etc.