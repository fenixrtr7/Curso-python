employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

def filter_salary(employee_list, salary_filter):
    return list(employee for employee in employee_list if employee['salary'] > salary_filter)

print(filter_salary(employees, 4000))