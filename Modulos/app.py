import reports
import finance

# Generar reposrte de ventas y gastos usando las funciones del módulo reports
sales_report = reports.generate_sales_report("January", 15000)
expenses_report = reports.generate_expenses_report("January", 5000)

print(sales_report)
print(expenses_report)

# Calcular el balance del mes usando la función del módulo finance
income = 15000 
expenses = 25000
balance = finance.calculate_balance(income, expenses)
print(f"Is the month profitable? {'Yes' if balance else 'No'}")
