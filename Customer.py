from LinkedList import LinkedList

class Customer:
    """Representa um cliente do supermercado."""


    def __init__(self, name):
        """
        Inicializa um cliente com nome e carrinho vazio.

        Args:
            name: Nome do cliente.
        """
        self.name = name
        self.cart = LinkedList() 
    
    def add_product(self, product):
        """
        Adiciona um produto ao carrinho do cliente.

        Args:
            product: Produto a ser adicionado.
        """
        self.cart.insert_end(product)  
    
    def total_value(self):
        """
        Calcula o valor total dos produtos no carrinho.

        Returns:
            Soma dos preços de todos os produtos.
        """
        return sum(p.price for p in self.cart.values())
    
    def __repr__(self):
        """Representação textual do cliente e valor total do carrinho."""
        return f"Customer {self.name}, total: ${self.total_value():.2f}"