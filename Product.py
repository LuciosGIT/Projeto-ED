class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"{self.code} - {self.name} (${self.price:.2f})"