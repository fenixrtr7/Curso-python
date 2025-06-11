class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
class ManagerEmployee:
    def __init__(self, employee_list: list):
        self.employee_list = employee_list

    def add_employee(self, employee: Employee):
        self.employee_list.append(employee)
        print(f'{employee.name} agregado')

    def remove_employee(self, employee: Employee):
        self.employee_list.remove(employee)
        print(f'{employee.name} removido')

if __name__ == "__main__":
    print('Empleados')
    emp1 = Employee("Arturo", 3000)
    employees = []
    manager = ManagerEmployee(employees)
    manager.add_employee(emp1)
    manager.remove_employee(emp1)