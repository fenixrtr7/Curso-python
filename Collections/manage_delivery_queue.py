from collections import deque

def manage_delivery_queue() -> deque:
    #Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4") # Agrega al final de la cola
    delivery_queue.appendleft("order_0") # Agregar al principio de la cola
    delivery_queue.pop() # Elimina del final
    delivery_queue.popleft() # Elimina del inicio
    return delivery_queue

queue = manage_delivery_queue()
print(queue)

