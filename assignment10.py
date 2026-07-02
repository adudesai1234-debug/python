         #---Shopping Cart---#


class ShoppingCart:
    def __init__(self, product, qty, price):
        self.product = product
        self.qty = qty
        self.price = price
    
    def total_cost(self):
        return self.qty * self.price
    
    def display_bill(self):
        print(f"Product: {self.product}")
        print(f"Qty: {self.qty} x ₹{self.price}")
        print(f"Total: ₹{self.total_cost()}")

cart = ShoppingCart("Laptop", 3, 20000)
cart.display_bill()