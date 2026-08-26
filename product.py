from typing import List
from functools import reduce

class Product:
    name: str
    price: float
    quantity: int
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
    
class Inventory:
    products: List[Product]
    
    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product):
        self.products.append(product)
        
    def show_products(self):
        for product in self.products:
            print(f"El nombre del producto es {product.name}, tiene un precio de {product.price} y hay un stock de {product.quantity}")
    
    def get_inventory_total_amount(self):
        total_amount = reduce(lambda acc, x: acc + (x.price * x.quantity), self.products, 0)
        print(f"El monto total del inventario es: {total_amount}")
        return total_amount
    
inventory = Inventory()
shampoo = Product('Shampoo', 1200, 3)
atun = Product('Atún', 800, 3)

inventory.add_product(shampoo)
inventory.add_product(atun)

inventory.show_products()

inventory.get_inventory_total_amount()
        
