import asyncio
import time
import random
import multiprocessing

# Función asíncrona para verificar el inventario
async def check_inventory(item):
    print(f'Verificando inventario para {item}')
    await asyncio.sleep(random.randint(3,6))
    print(f'Inventario verificado para {item}')
    #Simular disponibilidad del artículo
    return random.choice([True, False])

# Función asíncrona para procesar el pago
async def process_payment(order_id):
    print(f'Procesando pago para el pedido {order_id}')
    await asyncio.sleep(random.randint(2,5))
    print(f'Pago procesado para el pedido {order_id}')
    # Simular éxito del pago
    return True

#Función intensiva en CPU para calcular el total del pedido
def calculate_total(items):
    print(f'Calculando el costo total para {len(items)} artículos...')
    time.sleep(5)  # Simular tiempo de cálculo
    total = sum(item['price'] for item in items)
    print(f'Total calculado: {total}')
    return total

async def process_order(order_id, items):
    print(f'Iniciando procesamiento del pedido {order_id}')
    # Verificar inventario para cada artículo
    inventory_checks = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)

    if not all(inventory_results):
        print(f'Pedido {order_id} no puede ser procesado debido a falta de inventario.')
        
    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,))
    
    # Procesar el pago asincronicamente
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f'Pedido {order_id} procesado exitosamente. Total: {total}')
    else:
        print(f'Error al procesar el pago para el pedido {order_id}.')

async def main():
    orders = [
        {'id': 1, 'items': [{'name': 'Camisa', 'price': 20}, {'name': 'Pantalón', 'price': 30}]},
        {'id': 2, 'items': [{'name': 'Zapatos', 'price': 50}, {'name': 'Sombrero', 'price': 15}]},
        {'id': 3, 'items': [{'name': 'Chaqueta', 'price': 100}, {'name': 'Bufanda', 'price': 25}]}
    ]

    #Procesar multiples ordenes concurrentemente
    tasks = [process_order(order['id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

#Creamos el event loop
if __name__ == '__main__':
    asyncio.run(main())