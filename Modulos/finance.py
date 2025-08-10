# Que contenga funciones para calcular el balance de un mes (diferencia entre ingresos y gastos) y determinar si el mes ha sido rentable
#1. La funcion calculate_balance(income, expenses) debe devolver la diferencia entre ingresos y gastos
#2. Devolver 'True' si el balance es positivo y 'false' si es negativo

def calculate_balance(income, expenses):
    balance = income - expenses
    return balance > 0