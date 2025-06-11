class Empleado:
    def __init__(self, name, *skills, **details):
        self.name = name
        self.skills = skills
        self.details = details

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Skills: {self.skills}")
        print(f"Details: {self.details}")

# Creación de un objeto e instancia de la clase
empleado = Empleado("Carlos", "Python", "Java", "C++", age=30, city="Bogotá")
empleado.show_info()
