# Importar funciones del módulo ecommerce
from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sale
# Importar funciones del módulo ecommerce2
from ecommerce2.sales.orders import new_order, cancel_order, view_order
from ecommerce2.inventory.stock import show_stock, update_stock, delete_product 

add_product("Laptop", 10)
remove_product("Laptop")
process_sale("Laptop", 2)

new_order("12345", "John Doe", "Laptop", 2)
cancel_order("12345")
view_order("12345")

show_stock()
update_stock("Laptop", 5)  
delete_product("Laptop")