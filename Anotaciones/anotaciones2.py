def add_employee_ids(id1: int, id2 :int) -> int:
    return id1 + id2

class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola, me llamo {self.name}, tengo {self.age}"
    
    
        