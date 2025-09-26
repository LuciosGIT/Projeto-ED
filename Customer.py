from LinkedList import LinkedList

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = LinkedList() 
    
    def add_product(self, product):
        self.cart.insert_end(product)  
    
    def total_value(self):
        return sum(p.price for p in self.cart.values())
    
    def __repr__(self):
        return f"Customer {self.name}, total: ${self.total_value():.2f}"