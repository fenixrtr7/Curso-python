# Definir el decorador
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Accedio el empleado")
        resultado = func(*args, **kwargs)
        print("Terminando...")
        return resultado
    return wrapper

# Aplicar el decorador
@mi_decorador
def procesar_pago():
    print("Se ejecuto el programa...")

procesar_pago()