def mi_funcion(parametro):
    print(f"Procesando: {parametro}")

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función...")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función...")
        return resultado
    return wrapper

# Aplicar el decorador
@mi_decorador
def procesar_pago():
    print("Procesando pago...")

procesar_pago()
