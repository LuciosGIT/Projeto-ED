from LinkedList import LinkedList
from Queue import Queue


class Supermarket:
    def __init__(self):
        self.inventory = LinkedList()
        self.checkout_queue = Queue()
    
    def add_product(self, product):
        self.inventory.insert_end(product)  
    
    # Solução 2: Usar o método values() que já existe
    def find_product(self, code):
        for product in self.inventory.values():
            if product.code == code:
                return product
        return None
    
    def add_customer(self, customer):
        self.checkout_queue.enqueue(customer)
    
    def serve_customer(self):
        customer = self.checkout_queue.dequeue()
        if customer:
            print(f"Servindo {customer.name}. Total: ${customer.total_value():.2f}")
        else:
            print("Não há clientes na fila.")
