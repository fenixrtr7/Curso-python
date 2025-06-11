def verificar_acceso(func):
    def wrapper(empleado):
        if empleado.get('role') == 'admin':
            return func(empleado)
        else:
            print("Acceso denegado: solo los administradores pueden acceder.")
    return wrapper

@verificar_acceso
def eliminar_empleado(empleado):
    print(f"Empleado {empleado['nombre']} ha sido eliminado.")

admin = {'nombre': 'Carlos', 'role': 'admin'}
empleado = {'nombre': 'Ana', 'role': 'empleado'}

eliminar_empleado(admin)
eliminar_empleado(empleado)
