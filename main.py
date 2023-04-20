# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int
# The class should also have a method named "total_cost" that calculates 
# and returns the total cost of the product, which is the price multiplied by the quantity.

# Create a list of Product objects and write a function that takes this list as 
# input and returns the product with the highest total cost.

# Write a program that creates a list of 5 Product objects, prints out their
# attributes, and then calls the function to find the product with the highest total cost.

from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self, price: float, quantity: int) -> float:
        product_cost = price * quantity
        return product_cost
    
@dataclass
class ProductObjects:
    product_list: List[Product] = []

    def add_product(self, product_add_list: Product) -> None:
        self.product_list.append(product_add_list)

    def all_products(self) -> None:
        if not self.product_list:
            print("The product list is empty")
        else:
            for product_add_list in self.product_list:
                print(f"Product ID: {product_add_list.product_id}, name: {product_add_list.name}, price: {product_add_list.price}, quantity: {product_add_list.quantity}")


product = ProductObjects()
product_object1 = Product(1, "Toy car", 5.75, 15)
product_object2 = Product(2, "Shampoo", 5.2, 4)
product_object3 = Product(3, "Power bank", 15.15, 3)
product_object4 = Product(4, "Flash drive", 75.00, 1)
product.add_product(product_object1)
product.add_product(product_object2)
product.add_product(product_object3)
product.add_product(product_object4)
product.add_product()