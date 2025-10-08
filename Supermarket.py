from LinkedList import LinkedList
from Queue import Queue


class Supermarket:
    """Simulador de supermercado com estoque e atendimento de clientes."""


    def __init__(self):
        """Inicializa o supermercado com estoque vazio e fila de clientes."""
        self.inventory = LinkedList()
        self.checkout_queue = Queue()
    
    def add_product(self, product):
        """
        Adiciona um produto ao estoque.

        Args:
            product: Produto a ser adicionado.
        """
        self.inventory.insert_end(product)  
    

    def find_product(self, code):
        """
        Busca um produto pelo código no estoque.

        Args:
            code: Código do produto.

        Returns:
            Produto encontrado ou None se não existir.
        """
        for product in self.inventory.values():
            if product.code == code:
                return product
        return None
    
    def add_customer(self, customer):
        """
        Adiciona um cliente à fila do caixa.

        Args:
            customer: Cliente a ser adicionado.
        """
        self.checkout_queue.enqueue(customer)
    
    def serve_customer(self):
        """
        Atende o próximo cliente da fila, mostrando o valor total do carrinho.
        """
        customer = self.checkout_queue.dequeue()
        if customer:
            print(f"Servindo {customer.name}. Total: ${customer.total_value():.2f}")
        else:
            print("Não há clientes na fila.")
